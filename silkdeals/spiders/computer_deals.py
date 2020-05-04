# -*- coding: utf-8 -*-
import scrapy


class ComputerDealsSpider(scrapy.Spider):
    name = 'computer_deals'
    allowed_domains = ['slickdeals.net/computer-deals/']
    start_urls = ['http://slickdeals.net/computer-deals//']

    def parse(self, response):
        pass
