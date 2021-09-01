# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 13:24:36 2021

@author: claws
"""

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

html = 'https://www.newegg.com/p/pl?d=amd+gpu'

#opens connection grabs page
client = uReq(html)
page_html = client.read()
client.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#grabs each product
containers = page_soup.findAll('div', {"class":"item-container"})
contain = containers[0]

for container in containers:
   brand = contain.div.div.a.img["title"]
   
   title = contain.findAll("a", {"class":"item-title"})
   product_info = title[0].text
   
   price = contain.findAll("li",{"class":"price-current"}) 
   price[0].text.strip()  
   
   print("Brand: " + brand)
   print("Info: " + product_info)
   print("Price: " + price)