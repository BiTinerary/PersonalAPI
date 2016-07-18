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
	with open('C:/Users/G/Desktop/SendSMSPy/obfuscateMe.txt', 'r') as obfuscateMe:
		for lineA in obfuscateMe:
			NeedsEncryption = lineA
			#Cipher(NeedsEncryption)

	with open('C:/Users/G/Desktop/SendSMSPy/obfuscateEncryptionMe.txt', 'r') as obEncryptionMe:
		for lineB in obEncryptionMe:
			NeedsMoreEncryption = lineB
			#Cipher(NeedsMoreEncryption)
    
	with open('C:/Users/G/Desktop/SendSMSPy/SendTo.txt', 'r') as sendToNumba:
		for lineC in sendToNumba:
			SendTo = lineC
			#Cipher(SendTo)

	with open('C:/Users/G/Desktop/SendSMSPy/APIKey.txt', 'r') as APIKeyText:
		for lineD in APIKeyText:
			APIKey = lineD
			#Cipher(APIKey)
finally:
	obfuscateMe.close()
	obEncryptionMe.close()
	sendToNumba.close()

voice.login(NeedsEncryption, NeedsMoreEncryption)

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
	return 'Someone signed onto:\nUser: %s\nComputer: %s' % (ComputerName, UserName)

def Shutdown():
	UserName = os.getenv('USERNAME')
	ComputerName = os.environ['COMPUTERNAME']
	return 'Shutting down:\nUser: %s\nComputer: %s' % (ComputerName, UserName)

while True:
	#CommandList = ['Weather', "Logged", 'Shutdown', 'Reboot']
	#WeatherCommand = voice.search('Weather', 'Logged', 'Shutdown', 'Reboot')
	WeatherCommand = voice.search('Weather')
	LoggedCommand = voice.search('Logged')
	ShutDownCommand = voice.search('Shutdown')
	RebootCommand = voice.search('Reboot')
	
	if len(WeatherCommand) == 1:
		message = str(getTemp())
		voice.send_sms(SendTo, message)
		markAsRead()
		deleteReadMessages()
		print "Weather SMS Sent"
	elif len(LoggedCommand) == 1:
		message = str(newLogIn())
		voice.send_sms(SendTo, message)
		markAsRead()
		deleteReadMessages()
		print "Logged SMS Sent"
	elif len(ShutDownCommand) == 1:
		message = str(Shutdown())
		voice.send_sms(SendTo, message)
		markAsRead()
		deleteReadMessages()
		os.system('shutdown -r -t 0 -f')
	else:
		print 'Nuffin to see here'
		sleep(5)