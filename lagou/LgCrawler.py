import requests
import time
import random
import pymysql
import re
from pyecharts.charts import BMap, Map, Geo, Bar, Pie, PictorialBar, Boxplot, WordCloud
from pyecharts import options as opts
from pyecharts.globals import ChartType, ThemeType, SymbolType


class LgCrawler(object):
    conn = None
    cursor = None


    def __init__(self):

        self.conn = pymysql.connect("127.0.0.1", "root", "12345678", "lagou")
        self.cursor = self.conn.cursor()

    def insert(self):
        sql = 'INSERT INTO jobs (positionName,workYear,salary,city,education,positionAdvantage,companyLabelList,financeStage,companySize,industryField,firstType) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        self.cursor.execute(sql)
        self.conn.commit()
        pass

    def query(self, sql):

        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def crawler(self):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
            'Host': 'www.lagou.com',
            'Referer': 'https://www.lagou.com/jobs/list_python/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput=',
            'Cookie': 'user_trace_token=20200321120912-e091b8e2-ae3a-4e98-b8cc-7eda56613730; LGUID=20200321120912-103e3b3f-4b2d-4b40-aac8-de6f2151b52a; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1584763752; _ga=GA1.2.707847320.1584763752; _gid=GA1.2.1026377415.1584763752; index_location_city=%E5%85%A8%E5%9B%BD; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22170fb47eec2128-04c4426beb9ea8-396d7406-1764000-170fb47eec46c6%22%2C%22%24device_id%22%3A%22170fb47eec2128-04c4426beb9ea8-396d7406-1764000-170fb47eec46c6%22%7D; sajssdk_2015_cross_new_user=1; X_MIDDLE_TOKEN=b44cae2e06dda98341f7fda429c15d04; PRE_UTM=; PRE_HOST=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist%5Fpython%2Fp-city%5F0%3F%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; LGSID=20200321151013-aa659974-2803-4434-83e7-ed146560e5e0; PRE_SITE=; X_HTTP_TOKEN=f05004685d58bcda35257748511c75fb5b02e29508; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1584775254; _gat=1; LGRID=20200321152606-05042c06-9cea-4b97-9b47-908278188949',
            'X-Anit-Forge-Code': '0',
            'X-Anit-Forge-Token': 'None',
            'X-Requested-With': 'XMLHttpRequest'
        }
        page = 0
        totalCount = 1
        resultSize = 0
        while (page * resultSize) <= totalCount:
            page = page + 1
            url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"

            datas = {
                'first': 'false',
                'pn': page,
                'kd': 'python'
            }
            if page == 1:
                datas['first'] = 'true'

            html = requests.post(url, headers=headers, data=datas)
            result = html.json()

            if page == 1:
                totalCount = result['content']['positionResult']['totalCount']
                resultSize = result['content']['positionResult']['resultSize']

            jobs = result['content']['positionResult']['result']
            for job in jobs:
                job_array = [job['positionName'], job['workYear'], job['salary'], job['city'], job['education'],
                             job['positionAdvantage'], "|".join(job['companyLabelList']),
                             job['financeStage'], job['companySize'], job['industryField'], job['firstType']]

                self.cursor.execute(self.sql, tuple(job_array))
                self.conn.commit()

            r = random.randint(15, 30)
            time.sleep(r)


    def city(self):

        sql = 'select city, count(1) counts from jobs group by city'
        results = self.query(sql)

        c = (
            Geo()
                .add_schema(maptype="china")
                .add(
                "城市热力图",
                list(results),
                type_=ChartType.HEATMAP,
            )
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(
                visualmap_opts=opts.VisualMapOpts(),
            ).render("拉钩城市热力图.html")
        )

        sql = 'select city,counts from (select city, count(1) counts from jobs group by city) a order by counts desc limit 20'
        results = self.query(sql)
        citys = []
        values = []
        for row in results:
            citys.append(row[0])
            values.append(row[1])
        c = (
            Bar()
                .add_xaxis(citys)
                .add_yaxis("各城市的招聘数量 Top 20", values)
                .set_global_opts(
                xaxis_opts=opts.AxisOpts(name_rotate=60, name="城市", axislabel_opts={"rotate": 45})
            ).render("拉钩城市招聘图.html")
        )

    def education(self):
        sql = 'select education,count(1) counts from jobs group by education'
        results = self.query(sql)
        c = (
            Pie()
                .add("", list(results))
                .set_global_opts(title_opts=opts.TitleOpts(title='学历占比'))
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
                .render("拉勾学历.html")
        )


    def workYear(self):
        sql = 'select workYear,count(1) counts from jobs group by workYear'
        results = self.query(sql)
        c = (
            Pie()
                .add("", list(results))
                .set_global_opts(title_opts=opts.TitleOpts(title='工作经验占比'))
                                 .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}，{d}%"))
                                 .render("拉勾工作年限.html")
        )

    def field(self):
        sql = 'select industryField from jobs'
        results = self.query(sql)
        rows = []
        for row in results:
            r = row[0].replace(',', ' ').replace('丨', ' ').replace('、', ' ')
            rows.extend(r.split(' '))
        sum = {}
        for r in rows:
            num = sum.get(r, 0) + 1
            sum[r] = num
        tup = sorted(sum.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)
        sum = {}
        for k, v in tup[0:20]:
            sum[k + str(v)] = v
        location = list(sum.keys())
        values = list(sum.values())

        c = (
            PictorialBar()
                .add_xaxis(location)
                .add_yaxis(
                "",
                values,
                label_opts=opts.LabelOpts(is_show=False),
                symbol_size=18,
                symbol_repeat="fixed",
                symbol_offset=[0, 0],
                is_symbol_clip=True,
                symbol=SymbolType.ROUND_RECT,
            )
                .reversal_axis()
                .set_global_opts(
                title_opts=opts.TitleOpts(title="热门行业"),
                xaxis_opts=opts.AxisOpts(is_show=False),
                yaxis_opts=opts.AxisOpts(
                    axistick_opts=opts.AxisTickOpts(is_show=False),
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(opacity=0)
                    ),
                ),
            )
                .render("拉勾行业.html")
        )


    def salary(self):
        sql = 'SELECT workYear,replace(salary,\'k\',\'\') s FROM jobs group by workYear,salary order by workYear'
        results = self.query(sql)
        sum = {}
        for r in results:
            rs = r[1].split('-')
            a = sum.get(r[0], [])
            a.extend(rs)
            sum[r[0]] = a

        for k in sum:
            numbers = list(map(int, sum[k]))
            v = list(set(numbers))
            sum[k] = v

        print(list(sum.values()))

        c = Boxplot()
        c.add_xaxis(list(sum.keys()))
        c.add_yaxis("薪资与工作经验", c.prepare_data(list(sum.values())))
        c.set_global_opts(title_opts=opts.TitleOpts(title="薪资与工作经验"))
        c.render("拉勾薪资.html")

    def ciyun(self):
        sql = 'select positionAdvantage,companyLabelList from jobs'
        results = self.query(sql)
        data = {}
        for row in results:
            positionStr = re.sub('\W+', ' ', row[0])
            labelStr = re.sub('\W+', ' ', row[1])
            a = positionStr.split(' ')
            b = labelStr.split(' ')
            a.extend(b)
            for i in a:
                data[i] = data.get(i, 0) + 1
            sum = []
            for k in data:
                sum.append((k,data[k]))

        (
            WordCloud()
            .add(series_name="热点分析", data_pair=sum, word_size_range=[6, 66])
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="热点分析", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
                ),
                tooltip_opts=opts.TooltipOpts(is_show=True),
            )
            .render("拉勾福利.html")
        )


    def companySize(self):
        results = self.query('select companySize,count(1) counts from jobs group by companySize')
        c = (
            Pie()
                .add("", list(results))
                .set_global_opts(title_opts=opts.TitleOpts(title='企业大小'))
                                 .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}，{d}%"))
                                 .render("拉勾企业大小.html")
        )


    def financeStage(self):
        results = self.query('select financeStage,count(1) counts from jobs group by financeStage')
        c = (
            Pie()
                .add("", list(results))
                .set_global_opts(title_opts=opts.TitleOpts(title='企业融资占比'))
                                 .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}，{d}%"))
                                 .render("拉勾融资.html")
        )
if __name__ == '__main__':
    LgCrawler().field()
