# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 13:04:17 2021

@author: claws
"""
import requests
import urllib.robotparser
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

itemUrl = 'https://www.outletpc.com/cpus--processors--amd-am4.html'
r = requests.get(itemUrl)
print(itemUrl)

robotUrl = 'https://www.outletpc.com/robots.txt'
print(robotUrl)
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}

rb = requests.get(robotUrl, headers=headers)
test = rb.text
page = requests.get(itemUrl, headers=headers)
page_html = page.text
rp = urllib.robotparser.RobotFileParser()
rp.set_url(robotUrl)
rp.read()
fetchRobot = rp.can_fetch("", robotUrl)
print(fetchRobot)
fetchItem = rp.can_fetch("", itemUrl)
print(fetchItem)

item_info = []
price = []
ratings = []
upc = []
condition = []


html = urlopen(itemUrl)
bs = soup(html, 'html.parser')

page_soup = soup(page_html, "html.parser")

containers = page_soup.find_all("div", {"class":"price-info"})
product_info = containers.text
   
print(product_info)
