## What can it be used for?
The concept is very similar to text based banking, in practice. However, can be customized to perform other services. Such as...

**Mass Computer Automation**: Issue one command that triggers script/s on several computers simultaneously.  
ie: Computer repair, virus removal, anti virus installation, etc...  

**IOT Applications**: A minimal IOT trigger which is as secure as your email login and/or LAN credentials. Essentially, a text based CLI (aliases) which doesn't require internet on the go. Shut down home computer, Wake on lan, activate servo or solenoid.  

**Bandwidth efficiency**: Use what's already being paid for but might not normally be accessible. Use home internet to get bits of data rather than soaking up mobile data. Use in places with access to mobile phones but not internet?  

**Cloud computing concept**: A minimalist interface to a device that is capable of exponentially more computing power. ie: send text/picture/attachment from Nokia 3310 but return **only** the results of a machine learning computer.  
  
## Overview
Run while loop on Orangepi or equivalent SBC. Scan inbox of email.  
`if unread.message.exists? from: myphonenumber@mymetropcs.com` trigger respective linux command. Delete message.  
  
In other words, I send SMS to personal email. SBC detects it and fires off local bash/ruby/python script.  
Some of which do local things like shutdown any/all/specific computers running the script. Returns API call, the world is your oyster and Bobs your uncle.  

**Some more ideas:**  
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


