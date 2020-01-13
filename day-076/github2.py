# -*- coding: utf-8 -*-
import scrapy
import re

class Github2Spider(scrapy.Spider):
    name = 'github2'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/login']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response, # 自动从response中寻找form表单
            formdata={"login": "xxx@qq.com", "password": "xxx"},
            callback=self.after_login
        )
    # 登录成功之后操作
    def after_login(self, response):
        # 找到页面上的 Issues 字段并打印
        print(re.findall("Issues", response.body.decode()))