# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:11:27 2021

@author: Connor Lawson
sources: 
        book
        https://www.techwithtim.net/
        
additional work:
        made selenium serach for a item in the search bar
        made selenium click to the next page to grab more items.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import json
import numpy as np
import requests
from requests import get
from bs4 import BeautifulSoup

# with webdriver.Firefox() as driver:

headers = {"Accept-Language": "en-US,en;q=0.5"}

driver = webdriver.Firefox()

url = 'https://www.tigerdirect.com/'
driver.get(url)
print(driver.title)

search = driver.find_element_by_id("tigerv2_searchform")
search.send_keys("usb cable")
search.send_keys(Keys.RETURN)

data = []

def page_func():
    try:
        main = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "sku-display"))
        )
        
        items = main.find_elements_by_class_name("each-sku")
        for item in items:
            name = item.find_element_by_class_name("sku-nameSearch")
            price = item.find_element_by_class_name("price")
            rating = item.find_element_by_class_name("itemRating")
            stock = item.find_element_by_class_name("stock")
            model = item.find_element_by_tag_name("p")
            
            data.append({'Item':name.text, 'Price':price.text, 
                       'Rating':rating.text, 'Stock':stock.text,
                 'Model and Item Number':model.text})               
    except:
        driver.quit()
        
    time.sleep(5)
 
def next_page():
    pages = np.arange(1, 1001, 10)

    for page in pages: 
      
      page = requests.get("https://www.tigerdirect.com/applications/SearchTools/search.asp?page=" + str(page) + "&keywords=usb%20cable&sort=0&recs=10", headers=headers)
      
      soup = BeautifulSoup(page.text, 'html.parser')
      
      movie_div = soup.find_all('div', class_='lister-item mode-advanced')
      
      time.sleep(5)
data = []

page1 = page_func()

next_page()
page = page_func()


with open('final.json', 'w') as fp:
    json.dump(data, fp, indent=2)