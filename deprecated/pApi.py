from googlevoice import Voice,util
from time import sleep
import requests
import json
import os
from datetime import date
import calendar
#from Crypto.Cipher import AES
#import base64

voice = Voice()

try:
	currentWorkingDir = os.getcwd()
	w = open(currentWorkingDir + '/AllCredz.txt')
	voiceNumba = w.readline()
	pSWRD = w.readline()
	eMail = w.readline()
	endUserNumba = w.readline()
	aPIKey = w.readline()
	herNumba = w.readline()

finally:
	w.close()

voice.login(eMail, pSWRD)

def markAsRead():
	while True :
		folder = voice.search('is:unread')
		if folder.totalSize <= 0:
			break
			util.print_(folder.totalSize)
		for message in folder.messages:
			util.print_(message)
			message.delete(1)

def deleteReadMessages():
	for message in voice.sms().messages:
	    if message.isRead:
	        message.delete()

def newLogIn():
	UserName = os.getenv('USERNAME')
	ComputerName = os.environ['COMPUTERNAME']
	return 'Someone is logged onto:\nUser: %s\nComputer: %s' % (ComputerName, UserName)

def Shutdown():
	UserName = os.getenv('USERNAME')
	ComputerName = os.environ['COMPUTERNAME']
	return 'Shutting down:\nUser: %s\nComputer: %s' % (ComputerName, UserName)

def WOL():
	wol.send_magic_packet('%s') % (MAC) #, ip_address='XX.XX.XX.XX', port=7)
	return "Magic Packet Sent!"

def colorOfTheDay():
	dateToday = date.today()
	dayOfWeek = calendar.day_name[dateToday.weekday()]
	lowerDay = str(dayOfWeek.lower())

	dayDictionary = {"monday":"maroon", "tuesday":"pink", "wednesday":"green", "thursday":"orange", "friday":"blue", "saturday":"purple", "sunday":"pink"}

	for day, color in dayDictionary.iteritems():
		if str(day) == str(lowerDay):
			print day
			print color
			dayInSentence = str(day[0].upper() + day[1:])
			colorInSentece = str(color[0].upper() + color[1:])
			return "Color of the day for %s: %s" % (dayInSentence, colorInSentece)
		else:
			None

def Forecast(areaCode):
	areaCode = str(areaCode)
	forecast = requests.get('http://api.openweathermap.org/data/2.5/forecast?q='+ areaCode +',US&appid='+ aPIKey +'&mode=json&&units=imperial')
	jsonString = forecast.text[0:]
	parsedJson = json.loads(jsonString)
	location = parsedJson['city']['name']
	middayTomorrowList = parsedJson['list'][6]
	date = middayTomorrowList['dt_txt']
	lowAndHigh = [middayTomorrowList['main']['temp_max'], middayTomorrowList['main']['temp_min']]
	humidity = middayTomorrowList['main']['humidity']
	weather = [middayTomorrowList['weather'][0]['main'], middayTomorrowList['weather'][0]['description']]
	forecast.close()
	return str('Tomorrow in: %s\nTime: %s\nHigh: %s*F Low: %s*F\n%s, %s.\nHumidity: %s') % (location, date, lowAndHigh[0], lowAndHigh[1], weather[0], weather[1], humidity)

def Weather(areaCode):
	areaCode = str(areaCode)
	weatherRightNow = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ areaCode +',US&appid='+ aPIKey +'&mode=json&&units=imperial')
	jsonString = weatherRightNow.text[0:]
	parsedJson = json.loads(jsonString)
	location = parsedJson['name']
	condishList = parsedJson['main']
	tempHighLowAvg = [condishList['temp'], condishList['temp_max'], condishList['temp_min']]
	weatherList = parsedJson['weather'][0]
	weather = [weatherList['main'], weatherList['description']]
	humidity = condishList['humidity']
	weatherRightNow.close()
	return str('Today in: %s\nAverage: %s\nHigh: %s*F Low: %s*F\n%s, %s.\nHumidity: %s') % (location, tempHighLowAvg[0], tempHighLowAvg[1], tempHighLowAvg[2], weather[0], weather[1], humidity)

def getMessageDeets(htmlsms):
	phoneRegex = re.compile(r'\d\d\d\d\d\d\d\d\d\d\d')
	phoneRegex2 = re.compile(r'\(\d\d\d\)\s\d\d\d-\d\d\d\d')
	tree = BeautifulSoup.BeautifulSoup(htmlsms)
	findRawContact = tree.findAll('span', {'class' : 'gc-message-name'})
	searchPhoneRegex = phoneRegex.search(str(findRawContact))
	finalMatch = searchPhoneRegex.group()
	parseContact = tree.findAll('span', {'class' : 'gc-message-type'})
	stripExcess = str(parseContact).rstrip(" - mobile</span>]")
	finalParse = str(stripExcess).lstrip("[<span class=\"gc-message-type\">")

def getAddress():
		with open('curlOutput.txt', 'r') as f:
				fileIP = f.readline()
				#print('\nIP From File: ' + fileIP),

				urlGet = requests.get('https://icanhazip.com')
				actualIP = urlGet.text
				#print('Current IP: ' + actualIP)

				simpleFormatFileIP = str(fileIP).rstrip('\n')
				simpleFormatActualIP = str(actualIP).rstrip('\n')

				if simpleFormatFileIP != simpleFormatActualIP:
					print(simpleFormatFileIP + ' != ' + simpleFormatActualIP)
					messagez = "WRONG IPMAN!\nOld: %s\nNew: %s" % (simpleFormatFileIP, simpleFormatActualIP)
					f.close()
					with open('curlOutput.txt', 'r+') as f:
						f.write(simpleFormatActualIP)
						f.close()
					return messagez
					#return simpleFormatActualIP
				else:
					print(simpleFormatFileIP + ' == ' + simpleFormatActualIP)
					messagez = 'CORRECT IPMAN!\nOld: %s\nNew: %s' % (simpleFormatFileIP, simpleFormatActualIP)
					f.close()
					return messagez

while True:

	WeatherCommand = voice.search('Weather')
	ForecastCommand = voice.search('Forecast')
	LoggedCommand = voice.search('Logged')
	ShutDownCommand = voice.search('Shutdown')
	RebootCommand = voice.search('Reboot')
	WOLCommand = voice.search('WOL')
	SearchIP = voice.search('IPMAN')
	Color = voice.search('DAYCO')

	if len(WeatherCommand) == 1:
		message = str(Weather(55403))
		voice.send_sms(endUserNumba, message)
		markAsRead()
		deleteReadMessages()
		print "Weather SMS Sent"
	elif len(ForecastCommand) == 1:
		message = str(Forecast(55403))
		voice.send_sms(endUserNumba, message)
		markAsRead()
		deleteReadMessages()
		print "Forecast SMS Sent"
	elif len(WOLCommand) == 1:
		message = str(WOL())
		voice.send_sms(endUserNumba, message)
		markAsRead()
		deleteReadMessages()
	elif len(LoggedCommand) == 1:
		message = str(newLogIn())
		voice.send_sms(endUserNumba, message)
		markAsRead()
		deleteReadMessages()
		print "Logged SMS Sent"
	elif len(ShutDownCommand) == 1:
		message = str(Shutdown())
		voice.send_sms(endUserNumba, message)
		markAsRead()
		deleteReadMessages()
		os.system('shutdown -s -t 0 -f')
	elif len(SearchIP) == 1:
		message = str(getAddress())
		voice.send_sms(endUserNumba, message)
		markAsRead()
		deleteReadMessages()
		print "IPMAN SMS Sent"
	elif len(Color) == 1:
		message = str(colorOfTheDay())
		#voice.send_sms(herNumba, message)
		voice.send_sms(endUserNumba, message)
		markAsRead()
		deleteReadMessages()
	else:
		print 'Nuffin to see here'
		sleep(5)

"""
def Forecast(areaCode):
	areaCode = str(areaCode)
	forecast = requests.get('http://api.openweathermap.org/data/2.5/forecast?q='+ areaCode +',US&appid='+ aPIKey +'&mode=json&&units=imperial')
	jsonString = forecast.text[0:]
	parsedJson = json.loads(jsonString)
	location = parsedJson['city']['name']
	middayTomorrowList = parsedJson['list'][6]
	date = middayTomorrowList['dt_txt']
	lowAndHigh = [middayTomorrowList['main']['temp_max'], middayTomorrowList['main']['temp_min']]
	humidity = middayTomorrowList['main']['humidity']
	weather = [middayTomorrowList['weather'][0]['main'], middayTomorrowList['weather'][0]['description']]
	forecast.close()
	return str('Tomorrow in: %s\nTime: %s\nHigh: %s*F Low: %s*F\n%s, %s.\nHumidity: %s') % (location, date, lowAndHigh[0], lowAndHigh[1], weather[0], weather[1], humidity)

def Weather(areaCode):
	areaCode = str(areaCode)
	weatherRightNow = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ areaCode +',US&appid='+ aPIKey +'&mode=json&&units=imperial')
	jsonString = weatherRightNow.text[0:]
	parsedJson = json.loads(jsonString)
	location = parsedJson['name']
	condishList = parsedJson['main']
	tempHighLowAvg = [condishList['temp'], condishList['temp_max'], condishList['temp_min']]
	weatherList = parsedJson['weather'][0]
	weather = [weatherList['main'], weatherList['description']]
	humidity = condishList['humidity']
	weatherRightNow.close()
	return str('Today in: %s\nAverage: %s\nHigh: %s*F Low: %s*F\n%s, %s.\nHumidity: %s') % (location, tempHighLowAvg[0], tempHighLowAvg[1], tempHighLowAvg[2], weather[0], weather[1], humidity)
"""
"""
def getTemp():
	f = urllib2.urlopen('http://api.wunderground.com/api/'+ lineD +'/geolookup/conditions/q/MN/Minneapolis.json')
	json_string = f.read()
	parsed_json = json.loads(json_string)
	location = parsed_json['location']['city']
	temp_f = parsed_json['current_observation']['temp_f']
	condish = parsed_json['current_observation']['relative_humidity']
	weather = parsed_json['current_observation']['weather']
	return "%s:\nTemp: %s*F\nHumidity: %s\nWeather: %s" % (location, temp_f, condish, weather)
	f.close()
"""
"""
def Cipher(encryptme):
	BLOCK_SIZE = 32
	PADDING = '{'
	pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
	EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
	DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
	secret = os.urandom(BLOCK_SIZE)
	cipher = AES.new(secret)

	encoded = EncodeAES(cipher, encryptme)
	decoded = DecodeAES(cipher, encoded)
	return str(decoded)
"""
