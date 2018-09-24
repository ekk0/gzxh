# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 数据处理.py
import urllib.request

class GzxhPipeline(object):
    def process_item(self, item, spider):
        #写入文件
        localpath = "F:\GitHub\python\gzxh\gzxh\image\\"+item['name']+".jpg";
        #将数据写入文件夹
        urllib.request.urlretrieve(item['src'],localpath)
        print("----"+localpath)
        return item
