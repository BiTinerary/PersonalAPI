## pAPI: Porting from deprecated [pyGoogleVoice](https://pypi.python.org/pypi/pygooglevoice/0.5) library to [Gmail for Ruby](https://github.com/gmailgem/gmail)  

## Overview
Run while loop on Orangepi or equivalent SBC. Scan inbox of email. `if unread.message.exists? from: myphonenumber@mymetropcs.com` trigger respective linux command.  

Mark unread.message as read. Delete message. In other words, I send SMS to personal email. SBC detects it and fires off local bash/ruby/python script.  

Some of which do local things like shutdown any/all/specific computers. Returns API call, the world is your oyster.

## Why?
A minimal IOT interface which is as secure as your email login and/or LAN credentials. Triggered from what is essentially a text/SMS based CLI which doesn't require mobile internet. Further utilizing bandwidth that is paid for but might not normally be used.

**Some ideas:**  
`ipman` == then `curl icanhazip.com` and send SMS with response.  
`creditScore` == run webscrape script to get credit Score, current alerts, last opened account, identity scurity status, etc...  
`laidOff` == send out resume to specified email addresses.  
`weather 55108` == wunderground API response for zipcode  
`blackout` == run mass shutdown/kill command on device/s?  
`find regexForPhoneNumber` == response with Pipl.com api results.  

If command detected but from stranger number, send response after authentication on personal device?  
  
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

## TODO
* <strike>Don't login/logout for each key/value pair to avoid potential IMAP restrictions? Which might result from too many logins in X amount of time.
  * Login, search for all key/values, then logout and sleep. Or better yet, don't logout at all.</strike>
* omniauth integration
* <strike>'unread' message parsing</strike>
* <strike>main loop: `for message.each do |search keyword| end if keyword == 'shutdown' %x(shutdown now) end`</strike>
* <strike>Needs final while loop</strike>
* Test <strike>stdout vs other</strike> non echo command. Works, but needs more commands to be tested.
* <strike> House keeping: reorganize gmail session and login creds so it's not passed to so many other functions.</strike>


