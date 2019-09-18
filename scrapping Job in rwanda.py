# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 13:18:10 2019

@author: One Acre Fund
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 15:28:54 2019

@author: One Acre Fund
"""

import pandas as pd
from requests import get
from datetime import datetime
url = 'https://www.jobinrwanda.com/'
response = get(url)
from bs4 import BeautifulSoup
html_soup = BeautifulSoup(response.text, 'html.parser')
job_containers = html_soup.find_all('div', class_ ='media-body')
Job_title = []
Company = []
Deadline = []
experience = []

for job in job_containers:
    Job_title.append(job.h4.a.text)
    Company.append(job.select('a')[2].text)
    deadline = job.find('span', class_='date-display-single')
    Deadline.append(deadline.text)
    
for job in job_containers:
    brElements = job.find_all('br')
    for br in brElements:
        experience.append(br.next_sibling)
        
experience = [x.replace('\n', '').replace(' ', '') for x in experience]
for elem in experience :
    if elem == '':
        experience.remove(elem)

fullDataSet = pd.DataFrame({'POSITION':Job_title, 
                            'EMPLOYER':Company, 
                            'DEADLINE':Deadline,
                            'EXPERIENCE': experience})
    
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
#saveName = 'opportunity list as of' + dt_string +'.xlsx'
fullDataSet.to_excel('opportunity list one.xlsx')
print ('Success, Data scraped')