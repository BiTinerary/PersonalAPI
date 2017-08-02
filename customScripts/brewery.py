from brewerydb.brewerydb import BreweryDB
import json, sys

with open('./customScripts/config.json', 'r') as f:
    config = json.load(f)

brewAPI = BreweryDB(config['breweryDB'])

try: 
    beers = brewAPI.search_beer('%s' % sys.argv[1])
    beers = beers[0]
    website = beers.brewery["website"]
    breweryName = beers.brewery["name"]

    daGoodz = "Brew: %s\nName: %s\nABV: %s\nIBU: %s\nStyle: %s\nWebsite: %s\nImage: %s" % (breweryName, beers.name, beers.abv, beers.ibu, beers.style[0:20], website, beers.label_image_medium)
    print daGoodz
except:
    print "Beer not found."
