# -*- coding: utf-8 -*-
#项目源码地址：github.com/acredjb/FBP
#作者：acredjb
# scrapy crawl FBP -o BaseData.csv
import datetime
import sys
import requests
import scrapy
import time
import json
import scrapy.http
from peilv.items import PeilvItem
from lxml import etree
#获取当天或未来某天数据的地址
wl_url = 'https://live.leisu.com/saicheng?date='#wl历史https://live.leisu.com/saicheng?date=20190620
#获取历史数据的地址
ls_url = 'https://live.leisu.com/wanchang?date='#ls历史https://live.leisu.com/wanchang?date=20190606
class LiveJiangSpider(scrapy.Spider):
    name = 'FBP'
    allowed_domains = ['leisu.com']
    def start_requests(self):
            d1='20190606' #历史的比赛
            # d1='20190914' #未来的比赛
            request = scrapy.http.FormRequest(ls_url + d1,callback=self.parseLs, meta={'d1': d1}) #历史的比赛
            # request = scrapy.http.FormRequest(wl_url + d1,callback=self.parseWl, meta={'d1': d1})#未来的比赛
            yield request
    def parseLs(self,response):
        d2=response.meta['d1']
        sel=response.xpath
        racelist=[e5.split("'") for e5 in sel('//li[@data-status="8"]/@data-id').extract()]
        for raceid in racelist:#raceid=['2674547'];raceid[0]=2674547
            item = PeilvItem()
            sel_div=sel('//li[@data-id='+str(raceid[0])+']/div[@class="find-table layout-grid-tbody hide"]/div[@class="clearfix-row"]')
            if str(sel_div.xpath('span[@class="lab-lottery"]/span[@class="text-jc"]/text()').extract()) == "[]":
                item['cc']=""
            else:
                item['cc']=str(d2) + str(sel_div.xpath('span[@class="lab-lottery"]/span[@class="text-jc"]/text()').extract()[0])
            if "周" in item['cc']:#取竞彩-周一001等
                plurl='https://live.leisu.com/3in1-'+raceid[0]
                request = scrapy.http.FormRequest(plurl,callback=self.parse,meta={'item':item})
                yield request #并非return，yield压队列，parse函数将会被当做一个生成器使用。scrapy会逐一获取parse方法中生成的结果，并没有直接执行parse，循环完成后，再执行parse

    def parseWl(self,response):
        d2=response.meta['d1'] #接收参数
        sel=response.xpath
        racelist=[e5.split("'") for e5 in sel('//li[@data-status="1"]/@data-id').extract()]
        for raceid in racelist:#raceid=['2674547'];raceid[0]=2674547
            item = PeilvItem()
            sel_div=sel('//*[@data-id=' + str(raceid[0]) + ']/div[@class="find-table layout-grid-tbody hide"]/div[@class="clearfix-row"]')
            if str(sel_div.xpath('span[@class="lab-lottery"]/span[@class="text-jc"]/text()').extract()) == "[]":
                changci=""
            else:
                changci =str(sel_div.xpath('span[@class="lab-lottery"]/span[@class="text-jc"]/text()').extract()[0])

            if "周" in changci:#取竞彩-周一001等
                item['cc']=str(d2) + changci
                plurl='https://live.leisu.com/3in1-'+raceid[0]
                request = scrapy.http.FormRequest(plurl, callback=self.parse,meta={'item':item})
                yield request #并非return，yield压队列，parse函数将会被当做一个生成器使用。scrapy会逐一获取parse方法中生成的结果，并没有直接执行parse，循环完成后，再执行parse
    def parse(self, response):
        print('--------------into parse----------------------')
        item = response.meta['item']
        pv=response.xpath
        pl_str = '/td[@class="bd-left"]/div[@class="begin float-left w-bar-100 bd-bottom p-b-8 color-999 m-b-8"]/span[@class="float-left col-3"]/text()'

        if str(pv('//*[@data-id="5"]'+pl_str).extract())=="[]":
            item['li'] =  ''
        else:
            item['li']=pv('//*[@data-id="5"]' + pl_str).extract()[0]

        if str(pv('//*[@data-id="2"]'+pl_str).extract())=="[]":
            item['b5'] =  ''
        else:
            item['b5']=pv('//*[@data-id="2"]' + pl_str).extract()[0]

        yield item#程序在取得各个页面的items前，会先处理完之前所有的request队列里的请求，然后再提取items

