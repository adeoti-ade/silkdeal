# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector


class DealsSpider(scrapy.Spider):
    name = 'deals'

    def start_requests(self):

        yield SeleniumRequest(
            url = 'https://google.com',
            wait_time = 3,
            screenshot = True,
            callback=self.parse
        )

    def parse(self, response):
        
        # img = response.meta['screenshot']

        # with open('screenshot.png', 'wb') as f:
        #     f.write(img)

        driver = response.meta['driver']

        search_input = driver.find_element_by_xpath("//input[@class='gLFyf gsfi']")
        search_input.send_keys("Hello World!")

        # driver.save_screenshot("after_filling.png")

        search_input.send_keys(Keys.ENTER)
        # driver.save_screenshot("enter.png")

        html = driver.page_source
        html_response = Selector(text=html)

        links = html_response.xpath("//div[@class='r']/a")

        for link in links:
            yield {
                'url': link.xpath("./@href")
            }
