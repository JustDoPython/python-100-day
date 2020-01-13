import newspaper
from newspaper import news_pool
import requests
from newspaper import fulltext
from newspaper import Article

# 查看支持语言
# print(newspaper.languages())

# 获取新闻
# hq_paper = newspaper.build("https://tech.huanqiu.com/", language="zh", memoize_articles=False)
# for article in hq_paper.articles:
#     print(article.url)

# 获取类别
# for category in hq_paper.category_urls():
#     print(category)

# 获取品牌和描述
# print(hq_paper.brand)
# print(hq_paper.description)

# 下载解析
# article = hq_paper.articles[6]
# 下载
# article.download()
# 解析
# article.parse()
# 获取文章标题
# print("title=", article.title)
# 获取文章日期
# print("publish_date=", article.publish_date)
# 获取文章作者
# print("author=", article.authors)
# 获取文章顶部图片地址
# print("top_iamge=", article.top_image)
# 获取文章视频链接
# print("movies=", article.movies)
# 获取文章摘要
# print("summary=", article.summary)
# 获取文章正文
# print("text=", article.text)

# Article 类使用
# article = Article('https://money.163.com/19/1130/08/EV7HD86300258105.html')
# article.download()
# article.parse()
# print("title=", article.title)
# print("author=", article.authors)
# print("publish_date=", article.publish_date)
# print("top_iamge=", article.top_image)
# print("movies=", article.movies)
# print("text=", article.text)
# print("summary=", article.summary)

# nlp 处理
# print('处理前-->', article.keywords)
# article.nlp()
# print('处理后-->', article.keywords)

# 结合 requests 库解析文章
# html = requests.get('https://money.163.com/19/1130/08/EV7HD86300258105.html').text
# print('获取的原信息-->', html)
# text = fulltext(html, language='zh')
# print('解析后的信息', text)

# 多任务
# hq_paper = newspaper.build('https://www.huanqiu.com', language="zh")
# sh_paper = newspaper.build('http://news.sohu.com', language="zh")
# sn_paper = newspaper.build('https://news.sina.com.cn', language="zh")
# papers = [hq_paper, sh_paper, sn_paper]
# # 线程数为 3 * 2 = 6
# news_pool.set(papers, threads_per_source=2)
# news_pool.join()
# print(hq_paper.articles[0].html)

