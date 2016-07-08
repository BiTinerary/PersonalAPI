#Requirements:<br>
Windows for some hard coded commands.<br>
`pip install pygooglevoice`<br>
`pip install pycrypto`<br>
`pip install wakeonlan`<br>
(All others should be included in Python by default)<br>
~ A google voice account w/ specificed phone number (https://www.google.com/voice)<br>

Device that can be left on, connected to WiFi and run Python. ie:<br>
~ Raspi or equivalent SBC<br>
~ An extra Smartphone (capable of running QPython app)<br>

### Ideas Why?<br>
Send me a text if:<br>
~ <strike>My personal computer was just turned on.</strike> If it's not me, gather IP, geoloc, take webcam picture, etc... <strike>and force shutdown.</strike><br>
~ I want to send a <strike>magic packet to WOL<\strike> or WoWLAN<br> Note: Need to add external host, port forwarding, WOL.
~ <strike>I would like to know the weather. Is it going to rain? Good for biking to work?</strike><br>
~ Does my Wife need the car today based on her schedule? When does the next bus run by my house/leaving work?<br>
~ I'm supposed to be at work in an hour (which then sets off an alarm)<br>
~ I would like to know my current bank account balance/credit score/credit available<br>

#### Overall process<br>

~ `While` loop script to constantly check inbox of Google Voice <br>
~ `If` new message contains key word arguements (weather, parking, bank, alarm, jobshift, CreditScore, etc...) <br>
~ `Then` mark message as read, pass argument, send SMS containing requested web scraping material (use selenium/BeautifulSoup combo for high sec sites?)<br>
~ Delete messages `if` read<br>
~ Repeat loop <br>

# TODO
~ `Try/except` command on login script to `try urllib` command `except` `if` it spits an error because computer isn't connected to wifi. `Then` repeat `while` loop<br>

~ Add street parking command. `If` weather condish `==` severe snow warning, `then` 1st, 2nd, 3rd day? Send SMS with respective odd or even side of the street.<br>

~ Use `os.system` in conjunction with `if/else/try/except` to determine os and send shutdown command, etc...<br>

~ Computer repair command. W/portable Python or packaged `.exe`, run this script simultaneously on several computers (computer repair shop) `if` keyword `repair` is in GoogleVoice, run a/some basic diagnostics for each computer. HDD, RAM, VirusScan, etc.... Further `read` log files of portable progs (CrystalDiskInfo, NirSoft, etc...) that are generated automatically upon running. Via `json` module, `If` log file parameter contains "HDD Health Bad," collect. Rinse and Repeate. SMS the collective results.

~ Use `regex` (`import re`) to filter out Python syntax and match keywords. To pass different arguements based on GoogleVoice inbox. For instance `Weather('55406')` returns today's weather for saint paul. `Forecast('55416')` for 5 day of Saint Louis Park. Based on arguement, <strike>change Weather API</strike>, URL string to reflect parameters. 
