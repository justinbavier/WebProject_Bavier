import requests
import datetime
from bs4 import BeautifulSoup
import json
import csv

today = str(datetime.datetime.now().date())

# Create a list of dictionaries for JSON Object
response = []

# Scrape APNewsBriefs with requests
urlGreatNonProfits = 'http://greatnonprofits.org/city/nashville/TN'
pageGreatNonProfits = requests.get(urlGreatNonProfits)

# Prepare for parsing APNewsBriefs with BeautifulSoup
soupGreatNonProfits = BeautifulSoup(pageGreatNonProfits.content, 'lxml')

# Parse GreatNonProfits url
# 'position' marks the beginning of each news brief in the html
# All other data is found in its relationship to 'position'
for position in soupGreatNonProfits.find_all('li', class_='gnp-searchResult'):
    minorPosition = position.find('article').find('dl', class_='gnp-searchResult-infoMinor')
    name = position.find('div', class_='gnp-searchResult-infoMajor').find('a').string.split("                                            ")[1].split("                                        ")[0]
    city = position.find('article').find('div', class_='gnp-searchResult-location').find('span', property='addressLocality').string
    state = position.find('article').find('div', class_='gnp-searchResult-location').find('span', property='addressRegion').string
    page = 'http://greatnonprofits.org' + position.find('div', class_='gnp-searchResult-infoMajor').find('a').get('href')
    donate = 'http://greatnonprofits.org' + minorPosition.find('div', class_='gnp-searchResult-actions').find('a', class_='btn-donate').get('href')

    # Make changes to response for APNewsBriefs
    response.append({'Name': name, 'City': city, 'State': state, 'Page': page, 'Donate': donate})

# Write response to JSON file
postingsFile = today + '.GreatNonProfits.json'

#Write response to JSON file in another location
#postingsFile = '/APBriefs/' + today + '.APNewsBriefs.json'

with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()
