import requests, json, time, sys

with open('config.json', 'r') as f:
    config = json.load(f)

darkSkyKey = config['darkSkyKey']
geoLocKey = config['geoLocKey']
zipOrAddy = config['zipOrAddy']
responseFileName = config['responseFileName']

# Can omit getLatLon() function if only one location is required, however it's included for public reference.
def getLatLon(zipOrAddy, geoLocAPIKey): # Make Google GeoLocation API call for lat/long coordinates of almost any input. City, State, Address, ZIP, etc...
	response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' % (zipOrAddy, geoLocAPIKey)) # costs 1 call every execution.
	responseJson = response.json() # store response as json object, to be parsed.
	if responseJson['status'] == 'OK': # verifies a response has been successful. ie: Is your Zip or address even close?
		city = responseJson['results'][0]['address_components'][1]['short_name'] # City name
		state = responseJson['results'][0]['address_components'][3]['short_name'] # State abbreviation
		lat = responseJson['results'][0]['geometry']['location']['lat'] # lat value
		lon = responseJson['results'][0]['geometry']['location']['lng'] # lon value
		
		responseArray = [lat, lon, city, state]
		return responseArray

def coordinatesOf(zipOrAddy): # make a list from lat, lon, city and state without passing zip/API key more than once.
	coordinates = list(getLatLon(zipOrAddy, geoLocKey))
	return coordinates

def newResponse(): # make new API call, save results for offline reference. Keeps call limits for both API's to a minimum.
	weather = requests.get('https://api.darksky.net/forecast/%s/%s,%s' % (darkSkyKey, latLonCityState[0], latLonCityState[1]))

	with open(responseFileName, 'w+') as jsonFile:
		jsonFile.write(weather.content)
	#print '...results updated'
	return weather.content

def responseFile():
	with open(responseFileName) as read:
		goods = json.load(read)
	return goods

def fullSummary(theGoods): # get json minutely, hourly, daily summaries. ie: details for the hour, day, week/end.
	minHourDay = "%s %s %s" % (theGoods['minutely']['summary'], theGoods['hourly']['summary'], theGoods['daily']['summary'])
	print minHourDay

def dailyDetails(theGoods): # get percip, feels like, alerts. humidity, etc... for today.
	theGoodsCurrent = theGoods['currently']
	try:
		print theGoods['alerts'][0]['title'] # try to find weather warning alerts
		print theGoods['alerts'][0]['description']
	except: # if there are no weather warning alerts, don't error out. Continue main info output.
		print 'Today in %s, %s' % (latLonCityState[2], latLonCityState[3])
		print '------------------------'
		print theGoodsCurrent['summary']
		print 'Temp: %s Feels like: %s' % (theGoodsCurrent['temperature'], theGoodsCurrent['apparentTemperature'])
		print 'Humidity: %s Wind speed: %sMPH' % (theGoodsCurrent['humidity'], theGoodsCurrent['windSpeed'])
		print 'Percipitation: %s%%' % theGoodsCurrent['precipProbability']

		if theGoodsCurrent['precipProbability'] > 0: # if percipitation exists
			print "Rain intensity: %s" % theGoodsCurrent['precipIntensity'] # print intensity.

def getThreeDays(): # return specific json key/values for 3 days. Time, percip, etc...
	today = theGoods['daily']['data'][0] # today (zero is yesterday)
	tomorrow = theGoods['daily']['data'][1] # tomorrow
	third = theGoods['daily']['data'][2] # Trae day

	traeDays = [today, tomorrow, third]
	timeSummary = {}

	for day in traeDays: # for every day, convert epoch time, print specific details with layout.
		epoch = day['time']
		humanTime = time.strftime('%m.%d', time.localtime(epoch)) #returns midnight for each day %H:%M:%S
		summary = str(day['summary']) # sting because otherwise encoding prefixes values with unicode ie: u''
		percipProb = str(day['precipProbability'])
		percipIntensity = str(day['precipIntensity'])

		details = [summary, percipProb, percipIntensity]
		timeSummary[humanTime] = details

	#print '%s-%s in %s, %s' % (timeSummary.keys()[0], timeSummary.keys()[-1], latLonCityState[2], latLonCityState[3])
	print '3 Days in %s, %s' % (latLonCityState[2], latLonCityState[3])
	print '------------------------'
	for key, vals in timeSummary.iteritems():
		print "%s - %s Percip: %s Intensity: %s" % (key, vals[0], round(float(vals[1]), 2), round(float(vals[2]), 2))

if __name__ == "__main__":
	latLonCityState = coordinatesOf(zipOrAddy)
	#theGoods = responseFile() # default to offline parsing.
	theGoods = json.loads(newResponse()) # default to updating (1 API call) everytime script is run.

	try:
		if sys.argv[1] == 'summary':
			fullSummary(theGoods)
		elif sys.argv[1] == '3day':
			getThreeDays()
	except IndexError, e: # If nothing is passed, default to returning today's details.
		dailyDetails(theGoods)
		#print e

#https://darksky.net/poweredby/