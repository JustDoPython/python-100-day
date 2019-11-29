import newspaper
from newspaper import news_pool

hq_paper = newspaper.build('https://www.huanqiu.com', language="zh")
sh_paper = newspaper.build('http://news.sohu.com', language="zh")
sn_paper = newspaper.build('https://news.sina.com.cn', language="zh")

papers = [hq_paper, sh_paper, sn_paper]
# 线程数为 3 * 2 = 6
news_pool.set(papers, threads_per_source=2)
news_pool.join()
print(hq_paper.articles[0].html)