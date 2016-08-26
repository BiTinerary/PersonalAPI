from googlevoice import Voice
import sys
import BeautifulSoup
import re

def getMessageDeets(htmlsms):
    phoneRegex = re.compile(r'\d\d\d\d\d\d\d\d\d\d')
    phoneRegex2 = re.compile(r'\(\d\d\d\)\s\d\d\d-\d\d\d\d')


    def oneContactListed():
        tree = BeautifulSoup.BeautifulSoup(htmlsms)
        allspans = tree.findAll('span', {'class' : 'gc-nobold'})

        searchPhoneRegex = phoneRegex.search(str(allspans))
        #searchPhoneRegex2 = phoneRegex2.search(str(allspans))
        #print searchPhoneRegex
        finalMatch = searchPhoneRegex.group()
        #finalMatch2 = searchPhoneRegex2.group()
        #print finalMatch
        return finalMatch

    def twoContactListed():
        tree = BeautifulSoup.BeautifulSoup(htmlsms)
        spans = tree.findAll('span', {'class' : 'gc-message-type'})

        yo = str(spans).rstrip(" - mobile</span>]")
        heyo = str(yo).lstrip("[<span class=\"gc-message-type\">")
        #print heyo
        #print heyo
        return heyo,
        #return spans

    if len(oneContactListed()) == 10 or len(twoContactListed()) == 14:
        print oneContactListed()
        print twoContactListed()
        return 'supsupsupsupsusupsuspusp',
    else:
        return 'failed',

"""
    print finalMatch,
    print finalMatch2
    return finalMatch, finalMatch2,
"""
voice = Voice()
voice.login('izaac.kirscht@gmail.com', '#!Nunyabidnezz')

voice.sms()
for msg in getMessageDeets(voice.sms.html):
    print str(msg)