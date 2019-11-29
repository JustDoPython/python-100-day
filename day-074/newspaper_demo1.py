import newspaper

hq_paper = newspaper.build("https://tech.huanqiu.com/", language="zh", memoize_articles=False)
# for article in hq_paper.articles:
#     print(article.url)

# for category in hq_paper.category_urls():
#     print(category)

# print(hq_paper.brand)
# print(hq_paper.description)

article = hq_paper.articles[6]
# 下载
article.download()
# 解析
article.parse()
# 获取文章标题
print("title=", article.title)
# 获取文章日期
print("publish_date=", article.publish_date)
# 获取文章作者
print("author=", article.authors)
# 获取文章顶部图片地址
print("top_iamge=", article.top_image)
# 获取文章视频链接
print("movies=", article.movies)
# 获取文章摘要
print("summary=", article.summary)
# 获取文章正文
print("text=", article.text)
