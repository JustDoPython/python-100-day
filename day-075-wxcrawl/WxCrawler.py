# coding:utf-8
import requests
import re
import html
import demjson
import json
from bs4 import BeautifulSoup
import urllib3


class WxCrawler(object):
    urllib3.disable_warnings()

    #Hearders，x-wechat-key 会过期，会出验证问题
    headers = """Connection: keep-alive
        x-wechat-uin: MTY4MTI3NDIxNg%3D%3D
        x-wechat-key: 5ab2dd82e79bc534d85ba008887eba9adb87a0cab5737b646cd3841252f42348c3945407116dc4eff7f61dc2135c5329d73a04cf377d25083182103d343ae02171ce440e25e520d8530ff2d8f239e663
        Upgrade-Insecure-Requests: 1
        User-Agent: Mozilla/5.0 (Linux; Android 10; GM1900 Build/QKQ1.190716.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 XWEB/992 MMWEBSDK/191102 Mobile Safari/537.36 MMWEBID/7220 MicroMessenger/7.0.9.1560(0x27000933) Process/toolsmp NetType/WIFI Language/zh_CN ABI/arm64
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/wxpic,image/apng,*/*;q=0.8
        Accept-Encoding: gzip, deflate
        Accept-Language: zh-CN,en-US;q=0.9
        Cookie: wxuin=1681274216; devicetype=android-29; version=27000933; lang=zh_CN; pass_ticket=JvAJfzySl6uLWYdYwzyQ+4OqrqiZ2zfaI4F2OCVR7omYOmTjYNKalCFbr75X+T6K; rewardsn=; wxtokenkey=777; wap_sid2=COjq2KEGElxBTmotQWtVY2Iwb3BZRkIzd0Y0SnpaUG1HNTQ0SDA4UGJOZi1kaFdFbkl1MHUyYkRKX2xiWFU5VVhDNXBkQlY0U0pRXzlCZW9qZ29oYW9DWmZYOTdmQTBFQUFBfjD+hInvBTgNQJVO
        X-Requested-With: com.tencent.mm"""

    # 历史消息地址
    urls = "https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MjEwNDI4NTA2MQ==&scene=123&devicetype=android-29&version=27000933&lang=zh_CN&nettype=WIFI&a8scene=7&session_us=wxid_2574365742721&pass_ticket=JvAJfzySl6uLWYdYwzyQ%2B4OqrqiZ2zfaI4F2OCVR7omYOmTjYNKalCFbr75X%2BT6K&wx_header=1"

    #翻页地址
    page_url = "https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MjEwNDI4NTA2MQ==&f=json&offset=10&count=10&is_ok=1&scene=123&uin=777&key=777&pass_ticket=JvAJfzySl6uLWYdYwzyQ%2B4OqrqiZ2zfaI4F2OCVR7omYOmTjYNKalCFbr75X%2BT6K&wxtoken=&appmsg_token=1037_vtL%252FUIC6ITWXASKHcJqi9ml25Fys4vj-cW9X4w~~&x5=0&f=json"

    # 文章URL
    content_url_array = []

    def header_to_dict(self):
        headers = self.headers.split("\n")
        headers_dict = dict()
        for h in headers:
            k,v = h.split(":")
            headers_dict[k.strip()] = v.strip()

        return headers_dict;

    def article_list(self, context):
        articles = ""
        rex = "msgList = '({.*?})'"
        pattern = re.compile(pattern=rex, flags=re.S)
        match = pattern.search(context)
        if match:
            data = match.group(1)
            data = html.unescape(data)
            data = json.loads(data)
            articles = data.get("list")
        return articles

    def content_url(self, articles):
        for a in articles:
            a = str(a).replace("\/", "/")
            a = demjson.decode(a)
            self.content_url_array.append(a['app_msg_ext_info']["content_url"])
            # 取更多的
            for multi in a['app_msg_ext_info']["multi_app_msg_item_list"]:
                self.content_url_array.append(multi['content_url'])
                print(multi)

    def parse_article(self, headers, content_url):
        for i in content_url:
            content_response = requests.get(i, headers=headers, verify=False)
            with open("wx.html", "wb") as f:
                f.write(content_response.content)
            html = open("wx.html", encoding="utf-8").read()
            soup_body = BeautifulSoup(html, "html.parser")
            context = soup_body.find('div', id = 'js_content').text.strip()
            print(context)


    def page(self, headers):
        response = requests.get(self.page_url, headers=headers, verify=False)
        result = response.json()
        if result.get("ret") == 0:
            msg_list = result.get("general_msg_list")
            msg_list = demjson.decode(msg_list)
            self.content_url(msg_list["list"])
            #递归
            self.page(headers)
        else:
           print("无法获取内容")

    def run(self):
        headers = self.header_to_dict()

        response = requests.get(self.urls, headers=headers, verify=False)
        articles = self.article_list(response.text)
        self.content_url(articles)
        self.page(headers)
        self.parse_article(headers, self.content_url_array)



if __name__ == "__main__":

    wx = WxCrawler()
    wx.run()