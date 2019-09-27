# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 08:53:10 2019

@author: One Acre Fund
"""

import pandas as pd
from requests import get
from datetime import datetime
from bs4 import BeautifulSoup
url = 'http://recruitment.mifotra.gov.rw/Vacancies'
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
table = html_soup.find("table",class_="table table-condensed")

td_list = []  
td_cells = table.find_all('td')
for td_cell in td_cells:
    td_list.append(td_cell.text)
    
FullList = [x.replace('\n', '').replace(' ', '') for x in td_list]
FullList = [x.strip() for x in FullList]
output = [[]]
for x in FullList:
    output[-1].append(x)
    if x == 'Apply':
        output.append([])
        
clean_list = [x for x in output if x != []]

Employer = []
Deadline = []
Job_title = []

for x in clean_list:
    Employer.append(x[2])
    Deadline.append(x[3])
    Job_title.append(x[1])

fullDataSet = pd.DataFrame({'POSITION':Job_title, 
                            'EMPLOYER':Employer, 
                            'DEADLINE':Deadline})
    
fullDataSet.to_excel('public opportunity list one.xlsx')
print ('Success, Data scraped')
