#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""
import itchat
from matplotlib import pyplot as plt
import numpy as np
import jieba.analyse
from PIL import Image
import os
from matplotlib.font_manager import FontProperties
from wordcloud import WordCloud


class WxFriends:
    province_dict = {}
    friends = []
    province_tuple = ['北京', '上海', '天津', '重庆', '黑龙江', '吉林', '辽宁', '内蒙古', '河北',
                      '山东', '河南', '安徽','江苏', '浙江', '福建', '广东', '湖南', '湖北', '江西',
                      '宁夏', '甘肃', '新疆', '西藏', '青海', '四川','云南', '贵州', '广西', '山西',
                      '陕西', '海南', '台湾']

    # 登录
    @staticmethod
    def login():
        itchat.auto_login()

    # 爬取好友数据
    def crawl(self):
        friends_info_list = itchat.get_friends(update=True)
        print(friends_info_list[1])
        for friend in friends_info_list:

            print(friend['NickName'], friend['RemarkName'],  friend['Sex'],   friend['Province'],   friend['Signature'])

            # 处理省份
            if friend['Province'] in self.province_dict:
                self.province_dict[friend['Province']] = self.province_dict[friend['Province']] + 1
            else:
                if friend['Province'] not in self.province_tuple:
                    if '海外' in self.province_dict.keys():
                        self.province_dict['海外'] = self.province_dict['海外'] + 1
                    else:
                        self.province_dict['海外'] = 1
                else:
                    self.province_dict[friend['Province']] = 1

            self.friends.append(friend)

            # 保存头像
            img = itchat.get_head_img(userName=friend["UserName"])
            path = "./pic"
            if not os.path.exists(path):
                os.makedirs(path)
            try:
                file_name = path + os.sep + friend['NickName']+"("+friend['RemarkName']+").jpg"
                with open(file_name, 'wb') as f:
                    f.write(img)
            except Exception as e:
                print(repr(e))

    # 处理中文字体
    @staticmethod
    def get_chinese_font():
        return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

    # 为图表加上数字
    @staticmethod
    def auto_label(rects):
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x()+rect.get_width()/2.-0.2, 1.03*height, '%s' % float(height))

    # 展示省份柱状图
    def show(self):
        labels = self.province_dict.keys()
        means = self.province_dict.values()
        index = np.arange(len(labels)) + 1
        # 方块宽度
        width = 0.5
        # 透明度
        opacity = 0.4
        fig, ax = plt.subplots()
        rects = ax.bar(index + width, means, width, alpha=opacity, color='blue', label='省份')
        self.auto_label(rects)
        ax.set_ylabel('数量', fontproperties=self.get_chinese_font())
        ax.set_title('好友省份分布情况', fontproperties=self.get_chinese_font())
        ax.set_xticks(index + width)
        ax.set_xticklabels(labels, fontproperties=self.get_chinese_font())
        # 将x轴标签竖列
        plt.xticks(rotation=90)
        # 设置y轴数值上下限
        plt.ylim(0, 100)
        plt.tight_layout()
        ax.legend()

        fig.tight_layout()
        plt.show()

    # 分词
    @staticmethod
    def split_text(text):
        all_seg = jieba.cut(text, cut_all=False)
        all_word = ' '
        for seg in all_seg:
            all_word = all_word + seg + ' '

        return all_word

    # 作词云
    def jieba(self, strs):
        text = self.split_text(strs)
        # 设置一个底图
        alice_mask = np.array(Image.open('./alice.png'))
        wordcloud = WordCloud(background_color='white',
                              mask=alice_mask,
                              max_words=1000,
                              # 如果不设置中文字体，可能会出现乱码
                              font_path='/System/Library/Fonts/PingFang.ttc')
        myword = wordcloud.generate(str(text))
        # 展示词云图
        plt.imshow(myword)
        plt.axis("off")
        plt.show()

        # 保存词云图
        wordcloud.to_file('./alice_word.png')

    # 判断中文
    @staticmethod
    def judge_chinese(word):
        cout1 = 0
        for char in word:
            if ord(char) not in (97, 122) and ord(char) not in (65, 90):
                cout1 += 1
        if cout1 == len(word):
            return word

    # 处理签名，并生成词云
    def sign(self):
        sign = []
        for f in self.friends:
            sign.append(f['Signature'])

        strs = ''
        for word in sign[0:]:
            if self.judge_chinese(word) is not None:
                strs += word

        self.jieba(strs)

    # 主函数
    def main(self):
        self.login()
        self.crawl()
        self.show()
        self.sign()


if __name__ == '__main__':
    wxfriends = WxFriends()
    wxfriends.main()
