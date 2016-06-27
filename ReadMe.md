#Requirements:
pip install pygooglevoice
 
Ideally a Raspi or any small device capable of running a python while loop to check Google Voice for new messages.

## Over all plan

~ `While` loop script to constantly check inbox of Google Voice
~ `If` new message contains key word arguements (weather, parking, bank, alarm, jobshift, CreditScore, etc...)
~ `Then` mark message as read, pass argument, send SMS containing requested web scraping material (use selenium/BeautifulSoup combo for high sec sites?)
~ Delete messages `if` read
~ Repeat loop