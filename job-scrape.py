from bs4 import BeautifulSoup
import requests
import pandas as pd


def getSoup():
    #parse the soup

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}

    url = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword=software%20engineer&locT=C&locId=1154532&locKeyword=Boston,%20MA&srs=RECENT_SEARCHES'

    source = requests.get(url, headers=headers).text

    soup = BeautifulSoup(source, 'html.parser')

    return soup



def getTitleAndUrl(soup):
    jobTitle = {}
    jobLocation = {}
    jobEasyApply = {}
    jobURL = {}
    numJob = 0

    # for job in soup.findAll("h2", class_="title"):
    #     for title in job.findAll("a", class_="jobtitle"):
    #         titles[index] = (title['title'])
    #         links[index] = ('https://indeed.com'+title['href'])
    #     index += 1

    for li in soup.find_all(name="li", attrs={"class" : "react-job-listing css-wp148e eigr9kq3"}):
        jobTitle[numJob] = li['data-normalize-job-title']
        jobLocation[numJob] = li['data-job-loc']
        jobEasyApply[numJob] = li['data-is-easy-apply'] == "true"

        
        #["data-normalize-job-title"]
        #links[numJob] = li.find_all(name="a", aatrs={"class" : "css-jq9w1v jobLink css-1rd3saf eigr9kq2"})

        numJob += 1



    return (jobTitle, jobLocation, jobEasyApply)



def getCompanyName(soup):
    Company = {}
    return None




def main():
    soup = getSoup()
    ret = getTitleAndUrl(soup)
    print(ret)

main()