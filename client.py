
from bs4 import BeautifulSoup as bs
import requests
import json
import pprint

def get_linkedin_joblist_page_lxml(search_item, start):
    url = f"https://www.linkedin.co.uk/jobs/search/?keywords={search_item}?start={start}"
    response = requests.get(url)
    page = bs(response.content,'lxml')

    results = page.find_all('ul', class_='jobs-search__results-list')
    jobs = {}

    sublist = []

    ids = []
    for sub in results:
        for li in sub.find_all('li'):
            jobs[li['data-id']] = li.find('a', class_='result-card__full-card-link')['href']

    return jobs

def get_linkedin_job(url):
    response = requests.get(url)
    page = bs(response.content,'lxml')
    job_title = page.select('h1', class_='jobs-top-card__job-title t-24')[0].text.strip()
    #company = page.select('h3', class_='topcard__flavor-row')[1].find('a').text
    location = page.select('h3', class_='topcard__flavor-row')[1].find('span', class_='topcard__flavor topcard__flavor--bullet').text
    desc = page.select('div', id='job-details')
    description = [x for x in desc if x.find('div', class_="show-more-less-html__markup show-more-less-html__markup--clamp-after-5")][0].text
    result_dict = {'job_title':job_title, 'location':location, "job_desciption":description}
    return result_dict


def to_file(results,filename):
    with open(filename, 'a') as f:
        f.write(json.dumps(results))