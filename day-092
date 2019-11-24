#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2019-11-23 13:49:19
# Project: xinwen

import re

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=5 * 60)
    def on_start(self):
        self.crawl('http://www.chinashina.com/rexinwen/', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            if re.match(".*list_32_\d+\.html", each.attr.href, re.U):
                self.crawl(each.attr.href, callback=self.list_page)
        # 将第一页的抓取
        self.crawl(" http://www.chinashina.com/rexinwen/list_32_1.html", callback=self.list_page)
         
    @config(age=10 * 24 * 60 * 60)
    def list_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            if re.match(".*plus/view.php\?aid=\d+", each.attr.href, re.U):
                self.crawl(each.attr.href, callback=self.detail_page)
   
    @config(priority=2)
    def detail_page(self, response):
        return {
            "title": response.doc('.news_title').text(),
            "other": response.doc('html > body > .clearfix > .main_lt > div > .news_about > p').text(),
            "body": response.doc('html > body > .clearfix > .main_lt > div > .news_txt').text()
        }
