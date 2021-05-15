from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.glassdoor.com/Job/jobs.htm?sc.keyword=Software%20Engineer&suggestCount=0&suggestChosen=false&clickSource=searchBox').text

soup = BeautifulSoup(source, 'lxml')

jobs = soup.find('div')



print(jobs.prettify())