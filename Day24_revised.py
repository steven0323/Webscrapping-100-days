#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 11:33:59 2020

    @author: yu_hsuantseng
    Day 24 Rewriting Selenium 
"""
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import os
import pandas as pd
import numpy as np

# adding headers
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
def scroll_down():
    last_height = browser.execute_script("return document.body.scrollHeight")
    while True:

        # Scroll down to the bottom.
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page.
        time.sleep(2)
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

        

if __name__ == '__main__':
    
    url = "https://www.104.com.tw/cust/list/index/?page=1&order=1&mode=s&jobsource=checkc&area=6001001000&indcat=1001002000"
    browser = webdriver.Chrome(executable_path='./chromedriver')
    browser.get(url)
    
    while True:
        scroll_down()
        time.sleep(3)
        html = browser.page_source
        soup = BeautifulSoup(html, 'lxml')
        company_list = soup.find("div", attrs={'id':"company-result"}).find_all("article", attrs={'class':"items"})
        
        
        for company in company_list:
         
            company_name = company.a.string
            f = open("company_list.txt", "a+", encoding='utf-8')
            f.write( company_name + "\n" )  # 寫入公司名稱
            
            company_desc = company.find("p", attrs={'class':"desc"})
            f.write( company_desc.string + "\n" )  # 寫入公司簡介
            f.write( "--------------------------------------------------------------------------------" + "\n" )
            f.close()
        try:
            browser.find_element_by_class_name("page-next").click()
        except:
            print("next page does not exist")
            browser.quit()
            break