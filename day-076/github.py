# -*- coding: utf-8 -*-
import scrapy
import re

class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    # 登录页面 URL
    start_urls = ['https://github.com/login']

    def parse(self, response):
        # 获取请求参数
        commit = response.xpath("//input[@name='commit']/@value").extract_first()
        utf8 = response.xpath("//input[@name='utf8']/@value").extract_first()
        authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").extract_first()
        ga_id = response.xpath("//input[@name='ga_id']/@value").extract_first()
        if ga_id is None:
            ga_id = ""
        webauthn_support = response.xpath("//input[@name='webauthn-support']/@value").extract_first()
        webauthn_iuvpaa_support = response.xpath("//input[@name='webauthn-iuvpaa-support']/@value").extract_first()
        # required_field_157f = response.xpath("//input[@name='required_field_4ed5']/@value").extract_first()
        timestamp = response.xpath("//input[@name='timestamp']/@value").extract_first()
        timestamp_secret = response.xpath("//input[@name='timestamp_secret']/@value").extract_first()

        # 构造 post 参数
        post_data = {
            "commit": commit,
            "utf8": utf8,
            "authenticity_token": authenticity_token,
            "ga_id": ga_id,
            "login": "xxx@qq.com",
            "password": "xxx",
            "webauthn-support": webauthn_support,
            "webauthn-iuvpaa-support": webauthn_iuvpaa_support,
            # "required_field_4ed5": required_field_4ed5,
            "timestamp": timestamp,
            "timestamp_secret": timestamp_secret
        }

        # 打印参数
        print(post_data)

        # 发送 post 请求
        yield scrapy.FormRequest(
            "https://github.com/session", # 登录请求方法
            formdata=post_data,
            callback=self.after_login
        )

    # 登录成功之后操作
    def after_login(self, response):
        # 找到页面上的 Issues 字段并打印
        print(re.findall("Issues", response.body.decode()))