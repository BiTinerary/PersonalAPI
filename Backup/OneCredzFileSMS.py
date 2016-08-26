from googlevoice import Voice,util
from time import sleep
import requests
import json
import os

try:
	currentWorkingDir = os.getcwd()
	w = open(currentWorkingDir + '/AllCredz.txt')
	voiceNumba = w.readline()
	pSWRD = w.readline()
	eMail = w.readline()
	endUserNumba = w.readline()
	aPIKey = w.readline()
finally:
	w.close()

voice = Voice()
voice.login(eMail, pSWRD)
areaCode = 55403

def link():
	link = "http://api.openweathermap.org/data/2.5/forecast?q=%s,US&appid=%s&mode=json&&units=imperial" % (areaCode, aPIKey)
	return link

def Forecast(areaCode):
	areaCode = str(areaCode)
	forecast = requests.get(link())
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
	weatherRightNow = requests.get("http://api.openweathermap.org/data/2.5/forecast?q=%s,US&appid=%s&mode=json&&units=imperial" % (areaCode, aPIKey))
	jsonString = weatherRightNow.text[0:]
	parsedJson = json.loads(jsonString)
	location = parsedJson['city']['name']
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
	WeatherCommand = voice.search('Weather')
	ForecastCommand = voice.search('Forecast')
	LoggedCommand = voice.search('Logged')
	ShutDownCommand = voice.search('Shutdown')
	RebootCommand = voice.search('Reboot')
	WOLCommand = voice.search('WOL')

	if len(WeatherCommand) == 1:
		message = str(Weather(areaCode))
		voice.send_sms(endUserNumba, message)
		markAsRead()
		deleteReadMessages()
		print "Weather SMS Sent"
	elif len(ForecastCommand) == 1:
		message = str(Forecast(areaCode))
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
#from Crypto.Cipher import AES
#import base64

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