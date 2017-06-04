from brewerydb.brewerydb import BreweryDB
import sys

brew_api = BreweryDB('API KEY HERE')
try: 
    beers = brew_api.search_beer('%s' % sys.argv[1])
    beers = beers[0]
    website = beers.brewery["website"]
    breweryName = beers.brewery["name"]

    daGoodz = "Brew: %s\nName: %s\nABV: %s\nIBU: %s\nStyle: %s\nImage:\n%s" % (breweryName, beers.name, beers.abv, beers.ibu, beers.style[0:20], beers.label_image_medium)
    print daGoodz
except:
    print "Beer not found."