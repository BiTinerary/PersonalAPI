## What can it be used for?
The concept is very similar to text based banking, in practice. However, can be customized to perform other services. Such as...

**Mass Computer Automation**: Issue one command that triggers script/s on several computers simultaneously.  
ie: Computer repair, virus removal, anti virus installation, etc...  See: https://github.com/BiTinerary/BLDZRvZ

**IOT Applications**: A minimal IOT trigger which is as secure as your email login and/or LAN credentials. Essentially, a text based CLI (aliases) which doesn't require internet on the go. Shut down home computer, Wake on lan, activate servo or solenoid.  

**Bandwidth efficiency**: Use what's already being paid for but might not normally be accessible. Use home internet to get bits of data rather than soaking up mobile data. Use in places with access to mobile phones but not internet?  

**Cloud computing concept**: A minimalist interface to a device that is capable of exponentially more computing power.  
ie: send text/picture/attachment from Nokia 3310 but return **only** the results of a machine learning computer.  
  
## Overview
Run while loop on Orangepi or equivalent SBC. Scan inbox of email for keyword delivered by specified email address.  
`if unread.message.exists? from: myphonenumber@mymetropcs.com` trigger respective linux command. Delete message. Send alert to email address or phone number.   

**keyValuePairs.txt** contains a dictionary which keys pertain to the keyword that the script looks for in your inbox. If keyword is found, the respective value is the literal command to be executed. If this command has an output, this will be sent as an alert message to the recipient defined on the last line of **loginCreds.txt**.  

After the text files are read, **pAPI.rb** searches for the keywords provided. The search is done by the same GMail search function available from within the Web Browser GUI. Specifically `from: #{recipient} in:unread #{keyword}`. This disallows foreign emails from triggering commands and can also be scaled to include other Google search features like `has attachment`, `to:address@gmail.com`, date ranges and more.  

It's search regex can be loose or very specific. For instance, "Have you seen that new movie **ipman**" and simply "**ipman**" will both be enough to trigger a command. However, "**Computer1**" and "**Computer2**" allows seperately define commands to be run on specific computers. ie: Shutdown computer 1, reboot computer 2.

If these commands contain an output, send that information as notifications. This can be used for alerts or updates of online information, has the computer's internet been restored?, what is it's IP Address, return API like information. MAC Address, OS/System info, etc..? The world is your oyster and Bob's your uncle.  
  
**Some more ideas:**  
`ipman` == then `curl icanhazip.com` and send SMS with response.  
`creditScore` == run webscrape script to get credit Score, current alerts, last opened account, identity scurity status, etc...  
`laidOff` == send out resume to specified email addresses.  
`weather 55108` == wunderground API response for zipcode  
`blackout` == run mass shutdown/kill command on device/s?  
`find regexForPhoneNumber` == response with Pipl.com api results.  

If command detected but from stranger number, send response after authentication on personal device?  
Take arguments passed from email trigger. Parsing this email is tricky since MMS's sent from phone are base64 encoded along with something else.
  
## Requirements
* [Gmail For Ruby](https://github.com/gmailgem/gmail)  
	* Visit their repo for extensive example code for sending, reading, labelling, searching, deleting, etc... emails.
* [omniauth-google-oauth2](https://github.com/zquestz/omniauth-google-oauth2): To utilize oAuth2. Or not, if you wanna be the kinda person who stores credentials in plain text.  
	* Don't be that person
	* Visit their repo for setting up Google Developer API credentials, ID's, etc... for your gmail account.  
	* As well as example code for retrieving oAuth2 tokens.  
* [Rails](http://railsinstaller.org/en): Dependency of `omniauth-google-oauth2`  
* **loginCreds.txt** and **keyValuePairs.txt** files in same directory as script.
    * Make sure encoding is correct after you put in your specific credentials/changes.
    * These text file **names** are the only variables hardcoded into the script/executable.
  
## Executing

### On Linux based systems...  
`gem install gmail`  
`git clone https://github.com/BiTinerary/PersonalAPI`  
`cd PersonalAPI`  
`ruby pAPI.rb`  

### or on Windows..
`pApi.exe`  

## TODO
* Whitelist other addresses? Allows wife/coworker address to utilize tool. Reply to address sent from, not only from txt file.
* <strike>Don't login/logout for each key/value pair to avoid potential IMAP restrictions? Which might result from too many logins in X amount of time.
  * Login, search for all key/values, then logout and sleep. Or better yet, don't logout at all.</strike>
* omniauth integration
* <strike>'unread' message parsing</strike>
* <strike>main loop: `for message.each do |search keyword| end if keyword == 'shutdown' %x(shutdown now) end`</strike>
* <strike>Needs final while loop</strike>
* Test <strike>stdout vs other</strike> non echo command. Works, but needs more commands to be tested.
* <strike> House keeping: reorganize gmail session and login creds so it's not passed to so many other functions.</strike>


