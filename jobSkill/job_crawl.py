# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import random

urlFileName = 'shurls.txt'
contentFileName = 'context.txt'


def getUrls2Txt(page_num):

    p = page_num+1
    for i in range(1, p):
        urls = []
        # 抓取魔都的
        url = 'https://search.51job.com/list/020000,000000,0000,00,2,99,Python,2,'+str(i)+'.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='

        html = requests.get(url)
        soup = BeautifulSoup(html.content, "html.parser")
        ps = soup.find_all('p', class_='t1')
        for p in ps:
            a = p.find('a')
            urls.append(str(a['href']))
        with open(urlFileName, 'a', encoding='utf-8') as f:
            for url in urls:
                f.write(url+'\n')
        s = random.randint(5, 30)
        print(str(i)+'page done,'+str(s)+'s later')
        time.sleep(s)

def getContent(url, headers):
    record = ''
    try:
        html = requests.get(url, headers=headers)
        soup = BeautifulSoup(html.content, "html.parser")
        positionTitle = str(soup.find('h1')['title'])
        salary = soup.find_all('strong')[1].get_text()
        companyName = soup.find('p', class_='cname').get_text().strip().replace('\n','').replace('查看所有职位','')
        positionInfo = soup.find(
            'div', class_='bmsg job_msg inbox').get_text().strip().replace('\n', '').replace('分享', '').replace('举报', '').replace(' ', '').replace('\r', '')
        record = positionTitle + '&&&' + salary + '&&&' + companyName + '&&&' + '&&&' + positionInfo
    except Exception as e:
        print('错误了')
    return record


def main():
        page_num = 93
        getUrls2Txt(page_num)
        user_Agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        headers = {'User-Agent': user_Agent}
        with open(urlFileName, 'r', encoding='utf-8') as f:
            urls = f.readlines()
        i = 0
        for url in urls:
            url = url.strip()
            if url != '':
                record = getContent(url, headers)
                with open(contentFileName, 'a', encoding='utf-8') as f:
                        f.write(record + '\n')
                i += 1
                print(str(i)+'详情抓取完成')
                time.sleep(1)

        print('完成了')


if __name__ == '__main__':
    main()
