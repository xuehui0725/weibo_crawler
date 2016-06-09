# -*- coding: utf-8 -*-

import scrapy
import json

from weibo_crawler.items import weiboItem

class WeiboCrawler(scrapy.Spider):
    name = "weiboSpider"
    allowed_domains = ["http://m.weibo.cn/"]
    start_urls = [
        "http://m.weibo.cn/page/json?containerid=1005051687491394_-_WEIBO_SECOND_PROFILE_WEIBO&page=1"
    ]


    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        

