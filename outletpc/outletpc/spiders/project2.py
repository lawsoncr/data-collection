# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 13:11:45 2021

@author: Connor Lawson
"""

import scrapy
import json
from pprint import pprint


class OutletPCSpider(scrapy.Spider):
    name="OutletPCSpider"

    def start_requests(self):
        yield scrapy.Request('https://www.outletpc.com/__lsearch/?q=cable&size=15&storeid=outletpc&format=json')
        
    def parse(self, response):
        data =  json.loads(response.text)
        result = data["results"]
        pprint(result)
            
        url_list =[]
        for urls in result:
            yield{
                "Url" : urls["url"]
            }    
        
        
        
                    
            
            
        

        
        
##for loop to grab 100 pages 
        
##Grab 10 attributes