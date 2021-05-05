
from client import *
import time
import json

if __name__ == "__main__":
    
    # get list of jobs and dump them into a json file
    
    '''
    jobs = {}
    pagenum = 0
    
    search_term = 'devops'
    
    for _ in range(10):
        jobs.update(get_linkedin_joblist_page_lxml(search_term,pagenum))
        pagenum += 50
        time.sleep(30)
    print(len(jobs))
    to_file(jobs,'linkedin05052021.json')
    '''
    
    
    # get details from json file
    
    detail = []
    with open('linkedin05052021.json','r') as f:
        jobs = json.load(f)
    
    for id, url in jobs.items():
        try:
            detail.append([id, get_linkedin_job(url)])
        except:
            continue
    
    to_file(detail,'job_details05052021.json')
