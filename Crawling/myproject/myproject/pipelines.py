# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd

class MyprojectPipeline(object):

    def __init__(self):
        self.df = pd.DataFrame(columns=["body"])

    def process_item(self, item, spider):
        self.df = self.df.append(
            pd.DataFrame([[item["body"]]],
                         columns=["body"])
            , ignore_index=True)

        return item

    def close_spider(self, spider):
        # self.df.to_csv("wiki_kor.csv", sep=",", na_rep='NaN', encoding="UTF-8")
        self.df.to_csv("wiki_eng.csv", sep=",", na_rep='NaN', encoding="UTF-8")
