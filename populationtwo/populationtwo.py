#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""
import pandas as pd
import requests

# 人口数量excel文件保存路径
POPULATION_EXCEL_PATH = 'populationtwo.xlsx'

# 爬取人口数据
def spider_population():
    # 请求参数 sj（时间），zb（指标）
    # 总人口
    dfwds1 = '[{"wdcode": "sj", "valuecode": "LAST70"}, {"wdcode":"zb","valuecode":"A0301"}]'
    # 人口年龄结构和抚养比
    dfwds2 = '[{"wdcode": "sj", "valuecode": "LAST70"}, {"wdcode":"zb","valuecode":"A0303"}]'
    url = 'http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=sj&colcode=zb&wds=[]&dfwds={}'
    # 将所有数据放这里，年份为key，值为各个指标值组成的list
    # 数据顺序为历年数据
    population_dict = {

    }

    response1 = requests.get(url.format(dfwds1))
    get_population_info(population_dict, response1.json())

    response2 = requests.get(url.format(dfwds2))
    get_population_info(population_dict, response2.json())

    save_excel(population_dict)

    return population_dict

# 提取人口数量信息
def get_population_info(population_dict, json_obj):
    datanodes = json_obj['returndata']['datanodes']
    for node in datanodes:
        # 获取年份
        year = node['code'][-4:]
        # 数据数值
        data = node['data']['data']
        if year in population_dict.keys():
            population_dict[year].append(data)
        else:
            population_dict[year] = [int(year), data]
    return population_dict

# 人口数据生成excel文件
def save_excel(population_dict):
    # .T 是行列转换
    df = pd.DataFrame(population_dict).T[::-1]
    df.columns = ['年份', '年末总人口(万人)', '男性人口(万人)', '女性人口(万人)', '城镇人口(万人)', '乡村人口(万人)', '年末总人口(万人)', '0-14岁人口(万人)',
                  '15-64岁人口(万人)', '65岁及以上人口(万人)', '总抚养比(%)', '少儿抚养比(%)', '老年抚养比(%)']
    writer = pd.ExcelWriter(POPULATION_EXCEL_PATH)
    # columns参数用于指定生成的excel中列的顺序
    df.to_excel(excel_writer=writer, index=False, encoding='utf-8', sheet_name='中国70年人口数据')
    writer.save()
    writer.close()


if __name__ == '__main__':
    result_dict = spider_population()
    # print(result_dict)