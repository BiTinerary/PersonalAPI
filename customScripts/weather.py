import requests, json, time, sys

with open('./customScripts/config.json', 'r') as f:
	config = json.load(f, strict=False)

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
	print str(minHourDay)

def dailyDetails(theGoods): # get percip, feels like, alerts. humidity, etc... for today.
	theGoodsCurrent = theGoods['currently']
	try:
		print theGoods['alerts'][0]['title'] # try to find weather warning alerts
		print theGoods['alerts'][0]['description']
	except: # if there are no weather warning alerts, don't error out. Continue main info output.
		print 'Today in %s, %s' % (latLonCityState[2], latLonCityState[3])
		print '------------------------'
		print theGoodsCurrent['summary']
		print 'Temp: %s Feels: %s' % (theGoodsCurrent['temperature'], theGoodsCurrent['apparentTemperature'])
		print 'Humidity: %s Wind: %sMPH' % (theGoodsCurrent['humidity'], theGoodsCurrent['windSpeed'])
		print 'Percipitation: %s%%' % theGoodsCurrent['precipProbability']

		if theGoodsCurrent['precipProbability'] > 0: # if percipitation exists
			print "Rain intensity: %s" % theGoodsCurrent['precipIntensity'] # print intensity.

def getMultiDays(xDays): # return specific json key/values for 3 days. Time, percip, etc...
	xDays = int(xDays)
	
	daysForecast = []

	for each in xrange(xDays):
		day = theGoods['daily']['data'][each]
		daysForecast.append(day)

	timeSummary = {}

	for day in daysForecast: # for every day, convert epoch time, print specific details with layout.
		epoch = day['time']
		humanTime = time.strftime('%m.%d', time.localtime(epoch)) #returns midnight for each day %H:%M:%S
		summary = str(day['summary']) # sting because otherwise encoding prefixes values with unicode ie: u''
		percipProb = int(float(day['precipProbability']) * 100)
		percipIntensity = round(float(day['precipIntensity']), 2)
		humidity = day['humidity']
		windSpeed = day['windSpeed']
		highLow = [int(day['temperatureMin']), int(day['temperatureMax'])]
		feelsLike = int(int(day['apparentTemperatureMax']) + int(day['apparentTemperatureMax'])) / 2

		details = [summary, percipProb, percipIntensity, humidity, windSpeed, highLow, feelsLike]
		timeSummary[humanTime] = details

	#print '%s-%s in %s, %s' % (timeSummary.keys()[0], timeSummary.keys()[-1], latLonCityState[2], latLonCityState[3])
	print '%s Days in %s, %s' % (xDays, latLonCityState[2], latLonCityState[3])
	print '------------------------'
	for key, value in sorted(timeSummary.iteritems()):
		print "%s - %s High/Low: %s/%s Feels: %s\n%s%% chance of rain at %s mm/hr. %sMPH Winds. Humidity: %s\n" % (key, value[0], value[5][0], value[5][1], value[6], value[1], value[2], value[3], value[4])

if __name__ == "__main__":
	latLonCityState = coordinatesOf(zipOrAddy)
	#theGoods = responseFile() # default to offline parsing.
	theGoods = json.loads(newResponse()) # default to updating (1 API call) everytime script is run.

	try:
		if sys.argv[1] == 'summary':
			fullSummary(theGoods)
		elif sys.argv[1] == 'forecast':
			try:
				getMultiDays(sys.argv[2])
			except:
				print "Needs parameter or API didn't return enough days. Returning 3 days.\n"
				getMultiDays(3)

	except IndexError: # If nothing is passed, default to returning today's details.
		dailyDetails(theGoods)

#https://darksky.net/poweredby/
