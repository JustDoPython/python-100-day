import requests, time, random, pandas as pd
from lxml import etree

def spider():
    url = 'https://accounts.douban.com/j/mobile/login/basic'
    headers = {"User-Agent": 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'}
    # 安家评论网址，为了动态翻页，start 后加了格式化数字，短评页面有 20 条数据，每页增加 20 条
    url_comment = 'https://movie.douban.com/subject/30482003/comments?start=%d&limit=20&sort=new_score&status=P'
    data = {
        'ck': '',
        'name': '自己的用户',
        'password': '自己的密码',
        'remember': 'false',
        'ticket': ''
    }
    session = requests.session()
    session.post(url=url, headers=headers, data=data)
    # 初始化 4 个 list 分别存用户名、评星、时间、评论文字
    users = []
    stars = []
    times = []
    content = []
    # 抓取 500 条，每页 20 条，这也是豆瓣给的上限
    for i in range(0, 500, 20):
        # 获取 HTML
        data = session.get(url_comment % i, headers=headers)
        # 状态码 200 表是成功
        print('第', i, '页', '状态码：',data.status_code)
        # 暂停 0-1 秒时间，防止IP被封
        time.sleep(random.random())
        # 解析 HTML
        selector = etree.HTML(data.text)
        # 用 xpath 获取单页所有评论
        comments = selector.xpath('//div[@class="comment"]')
        # 遍历所有评论，获取详细信息
        for comment in comments:
            # 获取用户名
            user = comment.xpath('.//h3/span[2]/a/text()')[0]
            # 获取评星
            star = comment.xpath('.//h3/span[2]/span[2]/@class')[0][7:8]
            # 获取时间
            date_time = comment.xpath('.//h3/span[2]/span[3]/@title')
            # 有的时间为空，需要判断下
            if len(date_time) != 0:
                date_time = date_time[0]
                date_time = date_time[:10]
            else:
                date_time = None
            # 获取评论文字
            comment_text = comment.xpath('.//p/span/text()')[0].strip()
            # 添加所有信息到列表
            users.append(user)
            stars.append(star)
            times.append(date_time)
            content.append(comment_text)
    # 用字典包装
    comment_dic = {'user': users, 'star': stars, 'time': times, 'comments': content}
    # 转换成 DataFrame 格式
    comment_df = pd.DataFrame(comment_dic)
    # 保存数据
    comment_df.to_csv('data.csv')
    # 将评论单独再保存下来
    comment_df['comments'].to_csv('comment.csv', index=False)

spider()