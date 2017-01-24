import requests
from bs4 import BeautifulSoup

# Scrape GreatNonProfits with requests
# Name url
urlGreatNonProfits = 'http://greatnonprofits.org/city/nashville/TN'
# Scrap url with requests
pageGreatNonProfits = requests.get(urlGreatNonProfits)


# Prepare for parsing GreatNonProfits with BeautifulSoup
# soupGreatNonProfits is a BeautifulSoup object, created from the result of the request
# lxml is the parser we are using, works for html and xml
soupGreatNonProfits = BeautifulSoup(pageGreatNonProfits.content, 'lxml')

# Find position of middle portion of NonProfit Info Box
position = soupGreatNonProfits.find('li', class_='gnp-searchResult')
minorPosition = position.find('article').find('dl', class_='gnp-searchResult-infoMinor')

name = position.find('div', class_='gnp-searchResult-infoMajor').find('a').string.split("                                            ")[1].split("                                        ")[0]
city = minorPosition.find('div', class_='gnp-searchResult-location').find('span', property='addressLocality').string
state = minorPosition.find('div', class_='gnp-searchResult-location').find('span', property='addressRegion').string
page = 'http://greatnonprofits.org' + position.find('div', class_='gnp-searchResult-infoMajor').find('a').get('href')
donate = 'http://greatnonprofits.org' + minorPosition.find('div', class_='gnp-searchResult-actions').find('a', class_='btn-donate').get('href')

print(name)
print(city)
print(state)
print(page)
print(donate)

