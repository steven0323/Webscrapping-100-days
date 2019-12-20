#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 15:26:27 2019
    Day__13
@author: yu_hsuantseng
"""

import os
import sys
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
import numpy as np

url = 'https://www.ptt.cc/bbs/NBA/index.html'
r = requests.get(url)
soup = BeautifulSoup(r.text,'html5lib')
data_ = {'Author':[],'Title':[],'Time':[]}

for data in soup.find_all(class_="r-ent"):
    #print(data.text.replace('\t','').replace('\n',''))
    author = data.find('div',class_="author")
    Title = data.find('div',class_="title")
    Time = data.find('div',class_="date")
    
    data_['Author'].append(author.text.replace('\t','').replace('\n',''))
    data_['Time'].append(Time.text)
    data_['Title'].append(Title.text.replace('\t','').replace('\n',''))
    
df = pd.DataFrame(data_)
df = df = df.dropna(axis=0)

data  = {'Author':[],'Board':[],'Title':[],'Time':[],'Command':[]}
for d in soup.find_all(class_="title"):
    #print(d.text.replace('\t','').replace('\n',''))
    try:
        r = BeautifulSoup(requests.get("https://www.ptt.cc"+d.find('a')['href']).text,"html5lib")
        result = r.select('span.article-meta-value')
        if result:
           data['Author'].append(result[0].text)
           data['Board'].append(result[1].text)
           data['Title'].append(result[2].text)
           data['Time'].append(result[3].text)
           #print(result)
        #print(author)
        tag = r.find('div',class_="push")
        command = tag.find('span',class_="f3 push-content")
        #data['Command'].append(command)
    except:
        continue
#print(data)
df_1 = pd.DataFrame(data)