from googlevoice import Voice,util
from time import sleep
import urllib2
import json
import os
from Crypto.Cipher import AES
import base64

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

voice = Voice()


try:
	w = open('C:/Users/G/Desktop/SendSMSPy/AllCredz.txt')
	voiceNumba = w.readline()
	pSWRD = w.readline()
	eMail = w.readline()
	endUserNumba = w.readline()
	aPIKey = w.readline()
	CredzList = [voiceNumba, pSWRD, eMail, endUserNumba, aPIKey]
	#return voiceNumba, pSWRD, eMail, endUserNumba, aPIKey

finally:
	w.close()

voice.login(CredzList[2], CredzList[1])

def Forecast(areaCode):
	areaCode = str(areaCode)
	forecast = urllib2.urlopen('http://api.openweathermap.org/data/2.5/forecast?q='+ areaCode +',US&appid='+ aPIKey +'&mode=json&&units=imperial')
	jsonString = forecast.read()
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
	weatherRightNow = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ areaCode +',US&appid='+ aPIKey +'&mode=json&&units=imperial')
	jsonString = weatherRightNow.read()
	parsedJson = json.loads(jsonString)
	location = parsedJson['name']
	condishList = parsedJson['main']
	tempHighLowAvg = [condishList['temp'], condishList['temp_max'], condishList['temp_min']]
	weatherList = parsedJson['weather'][0]
	weather = [weatherList['main'], weatherList['description']]
	humidity = condishList['humidity']
	weatherRightNow.close()
	return str('Today in: %s\nAverage: %s\nHigh: %s*F Low: %s*F\n%s, %s.\nHumidity: %s') % (location, tempHighLowAvg[0], tempHighLowAvg[1], tempHighLowAvg[2], weather[0], weather[1], humidity)

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
	wol.send_magic_packet('%s') % (MAC)#, ip_address='XX.XX.XX.XX', port=7)
	return "Magic Packet Sent!"

while True:
	#CommandList = ['Weather', "Logged", 'Shutdown', 'Reboot']
	#for trigger in CommandList:
	#	voice.search(trigger)
	#WeatherCommand = voice.search('Weather', 'Logged', 'Shutdown', 'Reboot')
	WeatherCommand = voice.search('Weather')
	ForecastCommand = voice.search('Forecast')
	LoggedCommand = voice.search('Logged')
	ShutDownCommand = voice.search('Shutdown')
	RebootCommand = voice.search('Reboot')
	WOLCommand = voice.search('WOL')
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
	else:
		print 'Nuffin to see here'
		sleep(5)

"""
try:
	with open('obfuscateMe.txt', 'r') as obfuscateMe:
		for lineA in obfuscateMe:
			NeedsEncryption = lineA
			#Cipher(NeedsEncryption)

	with open('obfuscateEncryptionMe.txt', 'r') as obEncryptionMe:
		for lineB in obEncryptionMe:
			NeedsMoreEncryption = lineB
			#Cipher(NeedsMoreEncryption)
    
	with open('SendTo.txt', 'r') as sendToNumba:
		for lineC in sendToNumba:
			SendTo = lineC
			#Cipher(SendTo)

	with open('APIKey.txt', 'r') as APIKeyText:
		for lineD in APIKeyText:
			APIKey = lineD
			#Cipher(APIKey)
finally:
	obfuscateMe.close()
	obEncryptionMe.close()
	sendToNumba.close()
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