#Get first matched IP Address from twitter feed

import requests, re

urlString = requests.get('https://twitter.com/userNameHere')
daGoodz = urlString.content # get raw content, minus encoding *ish

iPRegex = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}') # IP Regex, could be shorter but c/would also be "moms spaghetti"
found = iPRegex.findall(daGoodz) # compare html string with regex.

urlLink = str('ftp://%s' % found[0]) # debug/print first instance of matched regex
print urlLink