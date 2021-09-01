# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 13:44:10 2021

@author: claws
"""


import scrapy 

class RedditbotSpider(scrapy.Spider):
    name = 'nasa'
    
    def start_request(self):
        yeild scrapy.Request('https://www.nasa.gov/missions', callback=self.parse)
        
    def parse(self, parse):
        response.css('a[href^="/mission_pages/]')        
    