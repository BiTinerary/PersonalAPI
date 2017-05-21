## pAPI: Ported from deprecated [pyGoogleVoice](https://pypi.python.org/pypi/pygooglevoice/0.5) library to [Gmail for Ruby](https://github.com/gmailgem/gmail)  

## Overview
Run while loop on Orangepi or equivalent SBC. Scan inbox of email. `if unread.message.exists? from: myphonenumber@mymetropcs.com` trigger respective linux command.  
Mark unread.message as read. Delete message.

**Some ideas:**  
I send SMS to personal email. SBC detects it. `If` content of message contains 'ipman', then `curl icanhazip.com` and send SMS with response.  
If content == 'weather'` send weatherunderground api response.  
If command detected from stranger number, send response after authentication on personal device.  
If command detected == `blackout` run mass shutdown/kill command on devices.  
If command == `find regexForPhoneNumber`, respons with Pipl.com api results.  
  
## Requirements
* [Gmail For Ruby](https://github.com/gmailgem/gmail)  
	* Visit their repo for extensive example code for sending, reading, labelling, searching, deleting, etc... emails.
* [omniauth-google-oauth2](https://github.com/zquestz/omniauth-google-oauth2): To utilize oAuth2. Or not, if you wanna hardcode and store credentials in clear text.  
	* Visit their repo for setting up Google Developer API credentials, ID's, etc... for your gmail account.  
	* As well as example code for retrieving oAuth2 tokens.  
* [Rails](http://railsinstaller.org/en): Dependency of `omniauth-google-oauth2`  
  
## Installation  
`gem install gmail`  
`git clone https://github.com/BiTinerary/PersonalAPI`


