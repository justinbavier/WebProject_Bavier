import requests
from bs4 import BeautifulSoup

# Scrape APNewsBriefs with requests
# Name url
urlAPNewsBriefs = 'http://hosted.ap.org/dynamic/fronts/HOME?SITE=AP&SECTION=HOME'
# Scrap url with requests
pageAPNewsBriefs = requests.get(urlAPNewsBriefs)


# Prepare for parsing APNewsBriefs with BeautifulSoup
# soupAPNewsBriefs is a BeautifulSoup object, created from the result of the request
# lxml is the parser we are using, works for html and xml
soupAPNewsBriefs = BeautifulSoup(pageAPNewsBriefs.content, 'lxml')

position = soupAPNewsBriefs.find('div', class_='ap-newsbriefitem')
headline = position.find('a').string
briefAndOffice = position.find('span', class_='topheadlinebody').string
brief = briefAndOffice.split(' - ')[1]
apOffice = briefAndOffice.split(' (AP) ')[0]
fullStory = 'http://hosted.ap.org' + position.find('a').get('href')
ctime = fullStory.split('CTIME=')[1]

print(headline)
print(brief)
print(apOffice)
print(fullStory)
print(ctime)
