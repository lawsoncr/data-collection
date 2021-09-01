# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:11:27 2021

@author: claws
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# with webdriver.Firefox() as driver:

driver = webdriver.Firefox()

url = 'https://www.tigerdirect.com/'
driver.get(url)
print(driver.title)

search = driver.find_element_by_id("tigerv2_searchform")
search.send_keys("usb cable")
search.send_keys(Keys.RETURN)


def page_func():
    try:
        main = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "sku-display"))
        )
        
        items = main.find_elements_by_class_name("each-sku")
        for item in items:
            name = item.find_element_by_class_name("sku-nameSearch")
            print("Item: ", name.text)
            price = item.find_element_by_class_name("price")
            print("Price: ", price.text)
            rating = item.find_element_by_class_name("itemRating")
            print("Rating: ", rating.text)
            stock = item.find_element_by_class_name("stock")
            print("Stock: ", stock.text)
            model = item.find_element_by_tag_name("p")
            print("Model and Item Number: ", model.text)
            print()
            
        
    except:
        driver.quit()
        
    time.sleep(5)

def next_page(num):
    try:
        n = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, num))
        )
        n.click()
           
    except:
            driver.quit()

page_func()
next_page("2")
page_func()
next_page("3")
page_func()
next_page("4")
page_func()
next_page("5")
page_func()
next_page("6")
page_func()
next_page("7")
page_func()
next_page("8")
page_func()
next_page("9")
page_func()
next_page("10")
page_func()