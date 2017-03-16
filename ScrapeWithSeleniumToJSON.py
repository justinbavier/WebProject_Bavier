from selenium import webdriver
import datetime
from bs4 import BeautifulSoup
import json
import time

# Create dict for JSON Object
response = []

# Prepare for parsing StackOverFlow with BeautifulSoup after Scraping with Selenium
browser = webdriver.Chrome()

url = 'http://stackoverflow.com/jobs?sort='

parse = True
i = 0
a = 0
# while parse == True:
while i < 2:
    page = browser.get(url)
    soup = BeautifulSoup(browser.page_source, 'lxml')

    # Parse StackOverFlow url.page_source
    for position in soup.find_all('div', class_='-job-info'):
        JobTitle = position.find('div', class_='-title').find('h2').find('a').string
        Salary = position.find('div', class_='-title').find('span', class_='salary')
        if Salary:
             Salary = Salary.string.split("\n                            ")[1].split("\n                    ")[0]
        else:
             Salary = "Not Listed"
        Employer = position.find('div', class_='-meta-wrapper').find('ul', class_='metadata primary').find('li', class_='employer').string.split("\n                        ")[1].split("\n                    ")[0]
        Location = position.find('div', class_='-meta-wrapper').find('ul', class_='metadata primary').find('li', class_='location').text.split("\n\n\n\n")[1].split("                    ")[0]
        Time = position.find('p', class_='text _small posted top').string.split("\n                    ")[1].split("\n                ")[0]
        if position.find('div', class_='tags') and position.find('div', class_='tags').find('a', class_='post-tag job-link no-tag-menu'):
            Tags = position.find('div', class_='tags').find('a', class_='post-tag job-link no-tag-menu')
            TagString = Tags.string
        else:
            TagString = "None"
            Tags = None

        while Tags:
            if Tags.next_sibling:
                TagString = TagString + ' ' + Tags.next_sibling.string
                Tags = Tags.next_sibling
            else:
                Tags = None
        a += 1
        a = a

        response.append({'Time': Time, 'Job Title': JobTitle, 'Employer': Employer, 'Location': Location, 'Tags': TagString, 'Salary': Salary})

    parse = False
    for nextPosition in soup.find_all('a', class_='prev-next'):
        if nextPosition.string == 'next':
            url = 'http://stackoverflow.com' + nextPosition.get('href')
            time.sleep(2)
            parse = True
            i += 1

browser.quit()

# Write response to JSON files
today = str(datetime.datetime.now().date())
postingsFile = '/Users/jbavi/PycharmProjects/WebProject_Bavier/stackoverflow_jobs/' + today + '.StackOverFlow.json'

with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()
