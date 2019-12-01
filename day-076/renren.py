# -*- coding: utf-8 -*-
import scrapy
import re

class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    # 个人中心页网址
    start_urls = ['http://www.renren.com/972990680/profile']

    def start_requests(self):
        # 登录之后用 chrome 的 debug 工具从请求中获取的 cookies
        cookiesstr = "anonymid=k3miegqc-hho317; depovince=ZGQT; _r01_=1; JSESSIONID=abcDdtGp7yEtG91r_U-6w; ick_login=d2631ff6-7b2d-4638-a2f5-c3a3f46b1595; ick=5499cd3f-c7a3-44ac-9146-60ac04440cb7; t=d1b681e8b5568a8f6140890d4f05c30f0; societyguester=d1b681e8b5568a8f6140890d4f05c30f0; id=972990680; xnsid=404266eb; XNESSESSIONID=62de8f52d318; jebecookies=4205498d-d0f7-4757-acd3-416f7aa0ae98|||||; ver=7.0; loginfrom=null; jebe_key=8800dc4d-e013-472b-a6aa-552ebfc11486%7Cb1a400326a5d6b2877f8c884e4fe9832%7C1575175011619%7C1%7C1575175011639; jebe_key=8800dc4d-e013-472b-a6aa-552ebfc11486%7Cb1a400326a5d6b2877f8c884e4fe9832%7C1575175011619%7C1%7C1575175011641; wp_fold=0"
        cookies = {i.split("=")[0]:i.split("=")[1] for i in cookiesstr.split("; ")}

        # 携带 cookies 的 Request 请求
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )

    def parse(self, response):
        # 从个人中心页查找关键词"闲欢"并打印
        print(re.findall("闲欢", response.body.decode()))
