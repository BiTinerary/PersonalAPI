<img src=='https://github.com/BiTinerary/PersonalAPI/customScripts/exampleScreenshot.png'>

## Why?
The concept is very similar to text based banking, in practice. However, can be customized to perform other services. Such as...

**Mass Computer Automation**: Issue one command that triggers script/s on several computers simultaneously.  
ie: Computer repair, virus removal, anti virus installation, etc...  See: https://github.com/BiTinerary/BLDZRvZ

**IOT Applications**: A minimal IOT trigger which is as secure as your email login and/or LAN credentials. Essentially, a text based CLI (aliases) which doesn't require internet on the go. Shut down home computer, Wake on lan, activate servo or solenoid. Send personalized alerts or updates containing sensor info.  

**Bandwidth efficiency**: Use what's already being paid for but might not normally be accessible. Use home internet to get bits of data rather than soaking up mobile data. Use in places with access to mobile phones but not internet?  

**Cloud computing concept**: A minimalist interface to a device that is capable of exponentially more computing power.  
ie: send text/picture/attachment from Nokia 3310 but return **only** the results of a machine learning computer.  
  
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
  
## Overview
Run while loop on Orangepi or equivalent SBC. Scan inbox for keyword delivered by specified email address. Trigger respective command. Delete message. Send alert to email address or phone number.  

**keyValuePairs.txt** contains a dictionary which key's pertain to the keyword that the script looks. If found, the respective value is the command to be executed. If this command has an output, this will be sent as a message to the recipient defined in **loginCreds.txt**.  

The inbox search is done by the same search function used in GMail's Web Browser UI. The specific search is `from: #{recipient} in:unread #{keyword}`. This disallows foreign emails from triggering commands and can also be scaled to include other Google search features like `has attachment`, `to:address@gmail.com`, date ranges and more. **Note**: the `from:` address can easily be spoofed.  

It's search regex can be loose or very specific but is mostly greedy. For instance, "Have you seen the movie **ipman**" and simply "**ipman**" will both trigger the same command. However, "**Computer1**" and "**Computer2**" allows seperately define commands to be run on specific computers. ie: Shutdown computer1, reboot computer2.
  
## Vulnerabilities
If a email/SMS is sent with content "PassArg(***echo Hellow Orld***)" then the command between the parens will be executed on the host machine. This arguably isn't necessarily a vulnerabilty in iteself but the fact that the sender email (`from: email.@email.com`) can easily be spoofed, is. No amount of oAuth2 or two factor authentication will change this vuln inside the code. Instead there will be changes to include the following:  
  
* Script will be used with an unpublicised, obfuscated email address.
* More obscure (not hardcoded [last arg in keyValuePairs?] customizeable) PassArg() variable.
* Make shift dual authentication from inside received message.
  * ie: Must end with special (changing) passcode defined in txt file.
* White/blacklist certain commands, "Are you sure you want to issue #{command} on #{system}? Y or N?", etc..  
* Custom scripting/sandboxing.
  * Should variable arguments need to be passed, write a script that takes sys.argv[1] but performs specific tasks.
  
All of that taken into account, this is why there are two versions included. One with/out the PassArg() capabilities. The keyValuePairs.txt acts as a sandbox for limiting the CLI to predefined commands/aliases. Whereas PassArg() expands the CLI to accept variables on host machine (ping 8.8.8.8 or curl www.website.com) but opens you up to a potential world of hurt. My suggestion is to make secondary scripts that can process these variables but perform very specific tasks. (send downloaded .apks/html's, curl output as attachments, etc...) Rather than allowing direct access to host Machine's CLI.

## Executing

### On Linux based systems...  
    gem install gmail  
    git clone https://github.com/BiTinerary/PersonalAPI  
    cd PersonalAPI  
    ruby pAPI.rb  

### or on Windows..
`pApi.exe`  

## TODO
* 'help' prompt, similiar to other text based services which gives user list of passable arguments and their features.
* <strike>Add function that allows custom arguments/commands to be sent to host computer **not** listed in keyValuePairs.txt
  * local computer commands that require variables. ie: ping www.google.com, whois ***8.8.8.8***</strike>
* Whitelist other addresses? Allows wife/coworker address to utilize tool. Reply to address sent from, not only from txt file.
* <strike>Don't login/logout for each key/value pair to avoid potential IMAP restrictions? Which might result from too many logins in X amount of time.
  * Login, search for all key/values, then logout and sleep. Or better yet, don't logout at all.</strike>
* omniauth integration
* <strike>'unread' message parsing</strike>
* <strike>main loop: `for message.each do |search keyword| end if keyword == 'shutdown' %x(shutdown now) end`</strike>
* <strike>Needs final while loop</strike>
* Test <strike>stdout vs other</strike> non echo command. Works, but needs more commands to be tested.
* <strike> House keeping: reorganize gmail session and login creds so it's not passed to so many other functions.</strike>

**Some ideas:**  
`someAndroidApp` == webscrape `appFileName.apk` and reply to phone with .apk ass attachment.
`ipman` == then `curl icanhazip.com` and send SMS with response.  
`creditScore` == run webscrape script to get credit Score, current alerts, last opened account, identity scurity status, etc...  
`laidOff` == send out resume to specified email addresses.  
`weather 55108` == wunderground API response for zipcode  
`blackout` == run mass shutdown/kill command on device/s?  
`find regexForPhoneNumber` == response with Pipl.com api results.  

If command detected but from stranger number, send response after authentication on personal device?  
Take arguments passed from email trigger. Parsing this email is tricky since MMS's sent from phone are base64 encoded along with something else.


