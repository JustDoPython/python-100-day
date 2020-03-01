import bs4 as bs4
import requests
import re
from requests import RequestException


'''
1、爬取豆瓣 250 电影数据 【名称，导演，国家，链接。上映时间，类型，评分[五星，四星占比]，评价人数】
2、数据分析
    上映时间
    类型
    评分
    五星，四星，三星，二星，一星占比
    评价人数
'''


def get_page_html(url):
    headers = {
        'Referer': 'https://movie.douban.com/chart',
        'Host': 'movie.douban.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def get_movie_url(html):
    ans = []
    soup = bs4.BeautifulSoup(html, 'html.parser')
    items = soup.select('li > div.item')
    for item in items:
        href = item.select('div.info > div.hd > a')[0]['href']
        ans.append(href)
    return ans


# 【名称，链接。导演，国家，上映时间，类型，评分，[五星，四星，三星，二星，一星占比]，评价人数】
def get_movie_info(url):
    html = get_page_html(url)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    content = soup.find('div', id='content')

    title = content.find('span', property='v:itemreviewed').text
    year = content.find('span', class_='year').text[1:5]
    directors = content.find('span', class_='attrs').find_all('a')
    director = []
    for i in range(len(directors)):
        director.append(directors[i].text)

    country = content.find(text=re.compile('制片国家/地区')).next_element
    typeList = content.find_all('span', property='v:genre')
    type = []
    for object in typeList:
        type.append(object.text)

    average = content.find('strong', property='v:average').text
    votes = content.find('span', property='v:votes').text

    rating_per_items = content.find('div', class_='ratings-on-weight').find_all('div', class_='item')
    rating_per = [rating_per_items[0].find('span', class_='rating_per').text, rating_per_items[1].find('span', class_='rating_per').text]

    return {'title': title, 'url': url, 'director': "#".join(director), 'country': country, 'year': year, 'type': "#".join(type),
            'average': average, 'votes': votes, 'rating_per': "#".join(rating_per)}


def main():
    urls = []
    for i in range(1):
        start = i * 25
        url = 'https://movie.douban.com/top250?start=' + str(start) + '&filter='
        html = get_page_html(url)
        urls.append(get_movie_url(html))

    index = 0;
    for url in urls:
        ans = get_movie_info(url)
        print(index, ans)
        index = index + 1


def getUrls():
    url_init = 'https://movie.douban.com/top250?start={0}&filter='
    urls = [url_init.format(index * 25) for index in range(10)]
    return urls

def writeToFile(content):
    filename = 'doubanTop250.txt'
    with open(filename,'a') as f:
        f.write(content + '\n')

if __name__ == '__main__':
    list_urls = getUrls()
    list_htmls = [get_page_html(url) for url in list_urls]
    movie_urls = [get_movie_url(html) for html in list_htmls]
    movie_url_list = []
    for url_list in movie_urls:
        movie_url_list += url_list

    for url in movie_url_list:
        print(url)

    movie_details = [get_movie_info(url) for url in movie_url_list]

    for detail in movie_details:
        writeToFile(str(detail))
        print(detail)


#print(get_movie_info('https://movie.douban.com/subject/1292052/'))