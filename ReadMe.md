#Requirements:
pip install pygooglevoice
(All others should be included in Python by default)
~ A google voice account w/ specificed phone number (https://www.google.com/voice)

Energy efficient device that can be left on and connected to WiFi connection which continuously runs a python script. ie:
~ Raspi or equivalent SBC
~ An extra Smartphone (capable of running QPython app)

### Ideas Why?
Send me a text if:
~ My personal computer was just turned on. If it's not me, gather IP, geoloc, etc... and force shutdown.
~ I would like to know the weather. Is it going to rain? Good for biking to work?
~ I'm supposed to be at work in an hour (which then sets off an alarm)
~ I would like to know when the next bus runs by my house/leaving work.
~ I would like to know my current bank account balance/credit score/credit available


#### Overall process

~ `While` loop script to constantly check inbox of Google Voice <br>
~ `If` new message contains key word arguements (weather, parking, bank, alarm, jobshift, CreditScore, etc...) <br>
~ `Then` mark message as read, pass argument, send SMS containing requested web scraping material (use selenium/BeautifulSoup combo for high sec sites?)<br>
~ Delete messages `if` read<br>
~ Repeat loop <br>
