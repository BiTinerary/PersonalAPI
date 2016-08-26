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
	with open('obfuscateMe.txt', 'r') as obfuscateMe:
		for lineA in obfuscateMe:
			NeedsEncryption = lineA
			Cipher(NeedsEncryption)

	with open('obfuscateEncryptionMe.txt', 'r') as obEncryptionMe:
		for lineB in obEncryptionMe:
			NeedsMoreEncryption = lineB
			Cipher(NeedsMoreEncryption)
    
	with open('SendTo.txt', 'r') as sendToNumba:
		for lineC in sendToNumba:
			SendTo = lineC
			Cipher(SendTo)

	with open('APIKey.txt', 'r') as APIKeyText:
		for lineD in APIKeyText:
			APIKey = lineD
			Cipher(APIKey)

finally:
	obfuscateMe.close()
	obEncryptionMe.close()
	sendToNumba.close()

voice.login(NeedsEncryption, NeedsMoreEncryption)

def newLogIn():
	UserName = os.getenv('USERNAME')
	ComputerName = os.environ['COMPUTERNAME']
	message = 'Someone signed onto:\nUser: %s\nComputer: %s' % (ComputerName, UserName)
	voice.send_sms(SendTo, message)
	print "Logged SMS Sent"

newLogIn()