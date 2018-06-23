#!/usr/bin/python
# -*- coding: utf-8 -*-
import scrapy
from crawler.items import CrawlerItem
from scrapy.http import Request
import pandas as pd
‘’‘
Movielens爬虫的主函数，爬取movielens数据集在IMDB中电影的评分，并存入CSV文件对应movieId的分数
’‘’

class MovieSpider(scrapy.Spider):
    name = 'crawler'
    allowed_domains = ['imdb.com']
    base_url = 'https://www.imdb.com/title/tt'
    links = pd.read_csv('E:/dataset/ml-latest/links.csv', usecols=[1], dtype={'imdbId': str})
    imdbdict = links.imdbId.tolist()

    def start_requests(self):
        for i in self.imdbdict:
            url = self.base_url + i
            yield Request(url, self.parse)

    def parse(self, response):
        items = CrawlerItem()
        imdbId = str(response.url)[-8:-1]
        items['imdbId'] = str(imdbId)
        score = response.xpath('//span[@itemprop="ratingValue"]/text()').extract()[0]
        items['score'] = score
        return items
