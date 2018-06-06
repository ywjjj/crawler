# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 爬取评分后存入csv文件
import csv
import itertools


class CrawlerPipeline(object):
    def __init__(self):
        self.csvwriter = csv.writer(open('E:/dataset/ml-latest/scores.csv', 'w', newline=''), delimiter=',')

    def process_item(self, item, spider):
        self.csvwriter.writerow((str(item['imdbId']), item['score']))
        print(str(item['imdbId']), '已经存入')
        return item
