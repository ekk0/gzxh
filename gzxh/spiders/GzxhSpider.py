# -*- coding: utf-8 -*-
#数据爬取.py
from gzxh.items import GzxhItem;
import  scrapy
class GzxhSpider(scrapy.Spider):
    name="gzxh"
    start_urls = ['http://www.521609.com/gaozhongxiaohua/list51.html']

    def parse(self, response):
        #返回一个list , xpath类型的
        content = response.xpath('//div[@class="index_img list_center"]/ul/li/a/img')
        for i in content:
            item = GzxhItem();
            item['name'] = i.xpath('@alt').extract()[0]
            item['src']  ="http://www.521609.com" + str(i.xpath('@src').extract()[0])
            yield item


        for page in range(1, 42):
            next_url = "http://www.521609.com/gaozhongxiaohua/list5" + str(page) + ".html"
            yield scrapy.http.Request(next_url, callback=self.parse);







