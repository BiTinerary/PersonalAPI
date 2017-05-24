## What can it be used for?
A remote shell that requires internet connection only one way. Ask the internet questions (Alexa, Google, etc... API) with only a text message. ie: places with access to mobile phones but not internet.

A universal computer remote. Are you simultaneously repairing 10+ computers like I used to? Don't install all virus removal software, anti virus, cleaner programs one by one on each machine. Just to uninstall some later. Issue one command from mobile phone and run it on all computers.

A minimal IOT interface which is as secure as your email login and/or LAN credentials. Triggered from what is essentially a text/SMS based CLI which doesn't require mobile internet. Further utilizing bandwidth that is paid for, but might not normally be used.

A cloud computing concept. What's the point if you have to sign up, register, tech guru your way into a cloud computer? The idea is to provide a minimalist interface to a super device that is capable of exponentially more computing power. ie: send text from Nokia 3310 (original) but return **only** the results of a 'machine learning' computer/algorithm.

## Overview
Run while loop on Orangepi or equivalent SBC. Scan inbox of email.  
`if unread.message.exists? from: myphonenumber@mymetropcs.com` trigger respective linux command.  

Mark unread.message as read. Delete message. In other words, I send SMS to personal email. SBC detects it and fires off local bash/ruby/python script.  

Some of which do local things like shutdown any/all/specific computers. Returns API call, the world is your oyster.

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
`cd PersonalAPI`  
`ruby pAPI.rb`

### or on Windows..
`pApiFinalized.exe`  
You may need to recreate input files (**loginCreds.txt**, **keyValuePairs.txt**) since github doesn't preserve return carriage `\r\n` in these files. However it was made for, tested, and debugged on a Windows systems. So make sure sure those return characters are included, even if they're invisible. 

## TODO
* <strike>Don't login/logout for each key/value pair to avoid potential IMAP restrictions? Which might result from too many logins in X amount of time.
  * Login, search for all key/values, then logout and sleep. Or better yet, don't logout at all.</strike>
* omniauth integration
* <strike>'unread' message parsing</strike>
* <strike>main loop: `for message.each do |search keyword| end if keyword == 'shutdown' %x(shutdown now) end`</strike>
* <strike>Needs final while loop</strike>
* Test <strike>stdout vs other</strike> non echo command. Works, but needs more commands to be tested.
* <strike> House keeping: reorganize gmail session and login creds so it's not passed to so many other functions.</strike>


