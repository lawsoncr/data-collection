# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 13:07:47 2021

@author: claws
"""

import scrapy


class HockeySpider(scrapy.Spider):
    name = 'sportsreference-hockey'

    def start_requests(self):
        urls = [
            'http://www.hockey-reference.com/leagues/NHL_2020_games.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
       print('response:', response)
       pass
