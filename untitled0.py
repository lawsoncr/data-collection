# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 13:30:11 2021

@author: claws
"""

import urllib.robotparser
import re
import requests
from requests import Session
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}
base_page = 'https://www.quanthockey.com'
robot_page = 'https://www.quanthockey.com/robots.txt'
index_page = 'https://www.quanthockey.com/nhl/records/nhl-players-all-time-points-leaders.html'
pages = []
data = []

def get_rp(robot_url):
    global headers
    print('Robot URL: ' + robot_url)
    print()
    r = requests.get(robot_url, headers=headers)
    rp = urllib.robotparser.RobotFileParser()
    rp.parse(r.text.split('\n'))
    print('Allow Robot to fetch robot.txt:',  rp.can_fetch('*', r.text))
    print()
    
def get_page(index_url):
    global headers
    print('Crawling ' + index_url + "...")
    print()
    r = requests.get(index_url, headers=headers)
    rp = urllib.robotparser.RobotFileParser()
    rp.parse(r.text)
    if(rp.can_fetch('*', r.text)) == True:
        html = requests.get(index_url)
        bs = BeautifulSoup(html.text, "html.parser")
        return bs
    else:
        return None

get_rp(robot_page)

s = Session()
s.get('https://www.quanthockey.com')

x = re.compile('^(/hockey-stats/en/profile)')
for links in get_page(index_page).find_all("a", href = x):
    if "href" in links.attrs:
        if links.attrs["href"] not in pages:
            next_page = links.attrs["href"]
            pages.append(next_page)

for i in range(50):
    n = get_page(base_page + pages[i])
    name = n.find(id="pp_title").text
    birthdate = n.find("time", itemprop="birthDate").text
    birthplace = n.find("span", itemprop="birthPlace").text
    position = n.find(id="player-bio").contents[6].split(',')[0]
    height = n.find(id="player-bio").contents[8].split('|')[0]
    weight = n.find(id="player-bio").contents[8].split('|')[1]
    print("Name: " + name)
    print("Birthdate: " + birthdate)
    print("Birthplace: " + birthplace)
    print("Position: " + position)
    print("Height: " + height.replace(" ", ""))