import requests
from datetime import datetime


def fetch(url):
    r = requests.get(url)
    print(r.text)

start = datetime.now()

for i in range(30):
    fetch('http://httpbin.org/get')

end = datetime.now()

print("requests版爬虫花费时间为：")
print(end - start)
