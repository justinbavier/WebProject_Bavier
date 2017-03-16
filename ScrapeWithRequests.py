import requests
import datetime

today = str(datetime.datetime.now()).split(' ')[0]

sites = {'Great Nonprofits': 'http://greatnonprofits.org/city/nashville/TN'}

for name, link in sites.items():
    response = requests.get(link)
    html = response.content


    fileName = today + '.' + name + '.html'
    outfile = open(fileName, "wb")
    outfile.write(html)
    outfile.close()
