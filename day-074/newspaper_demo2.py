import newspaper
from newspaper import Article

def newspaper_url(url):
    web_paper = newspaper.build(url, language="zh", memoize_articles=False)
    for article in web_paper.articles:
        newspaper_info(article.url)

def newspaper_info(url):
    article = Article(url, language='zh')
    article.download()
    article.parse()
    print("title=", article.title)
    print("author=", article.authors)
    print("publish_date=", article.publish_date)
    print("top_iamge=", article.top_image)
    print("movies=", article.movies)
    print("text=", article.text)
    print("summary=", article.summary)

if __name__ == "__main__":
        newspaper_url("https://tech.huanqiu.com/")