#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""
import requests
import json
from wordcloud import WordCloud
from matplotlib import pyplot as plt


class bdindex:
    # 搜索指数URL
    data_url = 'http://index.baidu.com/api/WordGraph/multi?wordlist[]={keyword}'
    # 检查关键词url
    check_url = 'http://index.baidu.com/api/AddWordApi/checkWordsExists?word=%s'
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
        "Cookie": 'PSTM=1579955530; BAIDUID=C98F0EF9DCB3FC7E06D3B0FA63695787:FG=1; BIDUPSID=1FB86823BF26D806A0117921DBD66135; BDSFRCVID=bpFOJeC62ZTm5dnuEvqKKASNJe3SOxnTH6aoprlQ5IIcI75XA-7tEG0P_U8g0KubIXdfogKKLgOTHPIF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJkf_D8XtK83fP36q470htFjMfQXetJyaR3UWpQvWJ5TMC_whlOFK-I0XHLjWUPf-eOW3C5dLxQ8ShPC-tnZ56Lv5tRT-xb83JbnbxO83l02VM7ae-t2ynLVbNJ324RMW23r0h7mWUJzsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJIjjCajTcQjN_qq-JQa5TbstbHaJOqD4-k-PnVHPKXhUce2bQHKKI_0-3LK-0_hC_lD6LKjI6XDGLHJ6DfHJuHoC_htD0tftbzBPcqb-F0hHc2bP0hb6nLMbTeqR3bJRO6q6KKDjjLDGtXJjDDtJCH_5u-tDDKhD_6eTONjbtpbtbmhU-e56vQ3-5SWfK2sKTn0qjTD5v3hh6aaTv45J7ZVDKbtI8MbDLrMRoVK-A0hxLXt6kXKKOLVb6Eb4OkeqOJ2Mt5bjFihp_O0PrXB6bCQCoTKlvRjPbzX4Oo0jtpeG_DtjFqtJksL-35HtnheJ54KPu_-P4DeU8eaMRZ5mAqoqOoyI_bO45ODtD2yU_9X467K5btX5rnaIQqabIMeMJFbnOIjqDNbbPtafc43bRT0xKy5KJvfjCx-UAMhP-UyPvMWh37Lg5lMKoaMp78jR093JO4y4Ldj4oxJpOJ5JbMopCafD_2MCD6DTLhen-W5gTEaPoX5Kj-WjrJabCQHnnph4Tqhh4ShUO-f6_jtnuf8JOSKRr_eJR3MPoB5P4XbacKJT3-5RPt3RLKfnD5MD89epDh0btpbtbmhU-e3TrOb45vK-oGbKjCKqo-2t0F-xbW2PkfaR7ZVD_ytCL-bK_GenJb5ICEbfreanLXKK_s3tJIBhcqEIL4WlOVjt0H5toqbxni0G7waJKbLh7WDxbSj4QoKbDj0HoAB4JAJbTv56C5bp5nhMJ33j7JDMP0-4rvKP5y523i2n3vQpnmOqQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0-nDSHHuOJjOP; BDUSS=UJsNmwzSnVwLWJ6eGJiTGtBMXRxVkNVVHFYOEgzZ0NMemo0V2o4dG9RaH5xbmxlRVFBQUFBJCQAAAAAAAAAAAEAAAArVO4Kzt7D-3ZpcGVyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH8dUl5~HVJee; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1582632851; bdshare_firstime=1582719699670; bdindexid=lbhlaubfjakm0eklbjbislhal1; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1582940553; delPer=0; PSINO=6; H_PS_PSSID=1445_21119_30790_30905_30823_26350; RT="sl=2&ss=k771w9qf&tt=1yz&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&z=1&dm=baidu.com&si=0pgwidvcjf8&ld=1ab9"',
        "Host": "index.baidu.com",
        "Referer": "http://index.baidu.com/v2/main/index.html"
    }

    # 获取指数数据
    def get_index(self, params):
        url = self.data_url.format(**params)
        response = requests.get(url, headers=self.headers)

        data = json.loads(response.text)['data']
        print(data)

        pv_dict = {}
        ratio_dict = {}
        for item in data['wordlist'][0]['wordGraph']:
            pv_dict[item['word']] = item['pv']
            ratio_dict[item['word']] = item['ratio']

        # 生成词云
        self.gen_wc_tags(pv_dict)
        self.gen_wc_tags(ratio_dict)

    # 检查关键词是否存在
    def check_word(self, kw):
        url = self.check_url % kw
        response = requests.get(url, headers=self.headers)
        data = json.loads(response.text)['data']
        return not len(data['result'])

    # 生成词云
    def gen_wc_tags(self, tags):
        # 设置一个底图
        # mask = np.array(Image.open('./bf.jpg'))
        wordcloud = WordCloud(background_color='black',
                              mask=None,
                              max_words=100,
                              max_font_size=100,
                              width=800,
                              height=600,
                              # 如果不设置中文字体，可能会出现乱码
                              font_path='/System/Library/Fonts/PingFang.ttc').generate_from_frequencies(tags)

        # 展示词云图
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()

        # 保存词云图
        wordcloud.to_file('./gzbd_wc.png')

if __name__ == '__main__':
    bdindex = bdindex()
    # keyword = '股市'
    # keyword = '新冠状病毒'
    keyword = '特朗普'
    word_exists = bdindex.check_word(keyword)
    if word_exists:
        params = {
            'keyword': keyword,
        }
        bdindex.get_index(params)
    else:
        print('keyword is not found')
