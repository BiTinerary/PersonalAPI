#Requirements:<br>
Windows for some hard coded commands.<br>
Use `os.system` in conjunction with `if/else/try/except` to determine os and send shutdown command, etc...<br>
`pip install pygooglevoice`<br>
`pip install pycrypto`<br>
(All others should be included in Python by default)<br>
~ A google voice account w/ specificed phone number (https://www.google.com/voice)<br>

Device that can be left on, connected to WiFi and run Python. ie:<br>
~ Raspi or equivalent SBC<br>
~ An extra Smartphone (capable of running QPython app)<br>
<br>
### Ideas Why?<br>
Send me a text if:<br>
~ My personal computer was just turned on. If it's not me, gather IP, geoloc, etc... and force shutdown.<br>
~ I want to send a magic packet to WOL or WoWLAN<br>
~ I would like to know the weather. Is it going to rain? Good for biking to work?<br>
~ I'm supposed to be at work in an hour (which then sets off an alarm)<br>
~ I would like to know when the next bus runs by my house/leaving work.<br>
~ I would like to know my current bank account balance/credit score/credit available<br>
<br>
#### Overall process<br>

~ `While` loop script to constantly check inbox of Google Voice <br>
~ `If` new message contains key word arguements (weather, parking, bank, alarm, jobshift, CreditScore, etc...) <br>
~ `Then` mark message as read, pass argument, send SMS containing requested web scraping material (use selenium/BeautifulSoup combo for high sec sites?)<br>
~ Delete messages `if` read<br>
~ Repeat loop <br>

# TODO
~ `Try/except` command on login script to `try urllib` command `except` `if` it spits an error because computer isn't connected to wifi. `Then` repeat `while` loop

~ Add street parking command. `If` weather condish `==` severe snow warning, `then` 1st, 2nd, 3rd day? Send SMS with respective odd or even side of the street.
