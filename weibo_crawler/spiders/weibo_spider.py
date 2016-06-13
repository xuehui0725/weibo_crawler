# -*- coding: utf-8 -*-

import scrapy
import json

from weibo_crawler.items import WeiboItem

class WeiboSpider(scrapy.Spider):
    name = "weiboSpider"
    # allowed_domains = ["http://m.weibo.cn/"]
    start_url = "http://m.weibo.cn/page/json?containerid=1005051687491394_-_WEIBO_SECOND_PROFILE_WEIBO&page=1"
    base_url = "http://m.weibo.cn/page/json?containerid=1005051687491394_-_WEIBO_SECOND_PROFILE_WEIBO&page="
    start_page = 1


    def start_requests(self):
        yield scrapy.Request(url=self.start_url, callback=self.parse)

    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        # 本页为空

        # 某页的微博列表
        page_info = jsonresponse["cards"][0]
        if page_info["mod_type"] == "mod/empty":
            return
        weibo_cards = page_info['card_group']

        for weibo_item in weibo_cards:
            item = WeiboItem()
            weiboContent = weibo_item["mblog"]
            item["dateTime"] = weiboContent["created_at"]
            item["text"] = weiboContent["text"]
            # print "dateTime:", item["dateTime"]
            # print "text:", item["text"]
            yield item

        self.start_page = self.start_page + 1
        next_url = self.base_url+str(self.start_page)
        print "next_url --- >:", next_url
        yield scrapy.Request(url=next_url, callback=self.parse)
