from googlevoice import Voice,util
from time import sleep

voice = Voice()

try:
	with open('obfuscateMe.txt', 'r') as obfuscateMe:
		for lineA in obfuscateMe:
			NeedsEncryption = lineA
    
	with open('obfuscateEncryptionMe.txt', 'r') as obEncryptionMe:
		for lineB in obEncryptionMe:
			NeedsMoreEncryption = lineB
    
	with open('SendTo.txt', 'r') as sendToNumba:
		for lineC in sendToNumba:
			sendTo = lineC

finally:
	obfuscateMe.close()
	obEncryptionMe.close()
	sendToNumba.close()

voice.login(NeedsEncryption, NeedsMoreEncryption)

while True:
	folder = voice.search('NuffinNuffin')
	if len(folder) == 1:
		print 'hellowzworld'
		message = 'HellowzWorld' #input('Message text: ')
		voice.send_sms(sendTo,message)
		sleep(5)
		continue
	else:
		print 'nuffin here to see'
		sleep(5)

"""
for message in voice.sms().messages:
    if message.isRead:
        message.delete()
"""