# Personal API
Use gmail to scan inbox for unread messages containing keywords. Trigger corresponding commands, scripts and alerts. Usage is very similar to text based banking, in practice, but can be customized to perform pretty much whatever.
  
<p align="center">
<img src='https://raw.githubusercontent.com/BiTinerary/PersonalAPI/master/customScripts/smallExampleScreenShots.png'>
</p>

## Why?
**Mass Computer Automation**: Issue one command that triggers script/s on several computers simultaneously.  
ie: Computer repair, virus removal, anti virus installation, etc...  See: https://github.com/BiTinerary/BLDZRvZ

**IOT Applications**: A minimal IOT trigger which is as secure as your email login and/or LAN credentials. Essentially, a text based CLI (aliases) which doesn't require internet on the go. Shut down home computer, Wake on lan, activate servo or solenoid. Send personalized alerts or updates containing sensor info.  

**Bandwidth efficiency**: Use what's already being paid for but might not normally be accessible. Use home internet to get bits of data rather than soaking up mobile data. Use in places with pay per GB ISP's? ie: Alaska. 

**Machine Learning in the Cloud Concept**: A minimalist interface to a device that is capable of exponentially more computing power. ie: send text/picture/attachment from Nokia 3310 but return **only** the results of a machine learning computer.
  
## Requirements
* [Gmail For Ruby](https://github.com/gmailgem/gmail)  
	* Visit their repo for extensive example code for sending, reading, labelling, searching, deleting, etc... emails.
* [omniauth-google-oauth2](https://github.com/zquestz/omniauth-google-oauth2): To utilize oAuth2. Or not, if you wanna be the kinda person who stores credentials in plain text.  
	* Don't be that person
	* Visit their repo for setting up Google Developer API credentials, ID's, etc... for your gmail account.  
	* As well as example code for retrieving oAuth2 tokens.    
* **loginCreds.txt** and **keyValuePairs.txt** files in same directory as script.
    * Make sure encoding is correct after you put in your specific credentials/changes.
    * These text file **names** are the only variables hardcoded into the script/executable.
  
## Overview
This is running continuously on a Orangepi board as a type of server which also handles 'home base' operations (IOT, WOL, Reed Switches) over VLAN, on top of RetrOrangePi.

Overall the ***pAPI.rb*** script is a while loop that scans inbox for keywords delivered by a specified email address. Trigger command/script. Delete message as to not rerun commands. ***keyValuePairs.txt*** contains a dictionary which key's pertain to the keyword that the script looks for. If found, it's respective value will be executed as a command. If this command has **stdout** or print statements, this will be sent to the recipient defined in ***loginCreds.txt***.

The inbox search is done by the same search function used in GMail's Web Browser UI.  
The specific search is `from: #{recipient} in:unread #{keyword}`. This can be scaled to include other Google search features like `has attachment`, `to:address@gmail.com` and more. **Note**: the `from:` address can easily be spoofed.  

The search regex can be loose or very specific but is mostly greedy. For instance, "Have you seen the movie **ipman**" and simply "**IPMAN**" will both trigger the same command. However, "**Computer1**" and "**Computer2**" allows seperately defined commands to be run on different hosts.
  
## Executing

### On Linux based systems...  
    gem install gmail  
    git clone https://github.com/BiTinerary/PersonalAPI  
    cd PersonalAPI  
    ruby pAPI.rb  

### or on Windows..
`pApi.exe`  

No it's not a signed .exe. Yes it's an exact copy of the **pAPI.rb** script. Don't wanna take my word for it? Roll your own. https://github.com/larsch/ocra  
    
    gem install ocra
    ocra customRubyScript.rb

## Vulnerability
The sender email (`from: email.@email.com`) can easily be spoofed which can result in giving others the ability to fire off any of the scripts. No amount of oAuth2 or two factor authentication will change this vuln inside the code. Instead, there are plans to make some of the following changes:  
  
* <strike>Script will be used with an unpublicised, obfuscated email address.</strike>
* More <strike>obscure triggering commands and variables.</strike>
* Dual authentication from inside received message.
  * ie: Must end with special (changing) passcode defined in txt file.
* White/blacklist certain commands, "Are you sure you want to issue #{command} on #{system}? Y or N?", etc..  
* <strike>Sandboxing. Only allow otherwise harmless commands/scripts to be executed. Weather, sensor data, etc...
  * Should variable arguments need to be passed, write a script that takes sys.argv[1] but performs specific tasks.</strike>
  
The ***keyValuePairs.txt*** acts as a sandbox for limiting the CLI to predefined aliases. Secondary scripts can process sent variables but perform very specific and harmless tasks. As seen in **./customScripts** folder. Paramters can be passed to custom Scripts. An example of this is sending BEER("Corona") as a message, the keyword BEER will be recognized by **brewery.py** Variable "Corona" will be parsed and passed as a parameter. So `python ./customScripts/brewery.py "Corona"` is literally being executed. The **`brewery.py`** uses BreweryDB API to return **.json** results of the IBU's, ABV, Name, image, Brewery of said beer. No I'm not that interested in beer, it's just an (enticing :P) example that I could throw together quickly to show API integration and outside error handling, while still restricting access.

## TODO
* Omniauth integration
* <strike>Allocate all credentials, API keys, oAuth (especially for customScripts) to one single file.</strike> 
* Whitelist other addresses? Allows wife/coworker's address to utilize tool? Reply to address sent from, not only from txt file.
* <strike>Add</strike> more '3rd party' script functionality.
  * <strike>These may seem hodge podge because they are. They're individual projects, worked on at different times.</strike>
  * <strike>Added to and most importantly coded at different levels of knowledge, patience, necessity, importance, etc...</strike>
* <strike>'help' prompt, similiar to other text based services which gives user list of passable arguments and their features.</strike>
* <strike>Add function that allows custom arguments/commands to be sent to host computer **not** listed in keyValuePairs.txt
  * local computer commands that require variables. ie: ping www.google.com, whois ***8.8.8.8***</strike>
* <strike>Don't login/logout for each key/value pair to avoid potential IMAP restrictions? Which might result from too many logins in X amount of time.
  * Login, search for all key/values, then logout and sleep. Or better yet, don't logout at all.</strike>
* <strike>'unread' message parsing</strike>
* <strike>main loop: `for message.each do |search keyword| end if keyword == 'shutdown' %x(shutdown now) end`</strike>
* <strike>Needs final while loop</strike>
* <strike>Test stdout vs other non echo command. Works, but needs more commands to be tested. </strike>
* <strike> House keeping: reorganize gmail session and login creds so it's not passed to so many other functions.</strike>

**Some ideas:**  
`reminder` == send emails/messages in the future.  
`someAndroidApp` == webscrape `appFileName.apk` and reply to phone with .apk ass attachment.  
<strike>`ipman` == then `curl icanhazip.com` and send SMS with response.</strike>  
<strike>`creditScore` == run webscrape script to get credit Score, current alerts, last opened account, identity scurity status, etc...</strike>  
<strike>`laidOff` == send out resume to specified email addresses.</strike>
<strike>`weather 55108` == wunderground API response for zipcode </strike>  
`blackout` == run mass shutdown/kill command on device/s?  
`find regexForPhoneNumber` == response with Pipl.com api results.  

If command detected but from foreign number, send response after authentication on personal device? 
