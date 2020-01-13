# 使用两种爬虫代理分别查看是否可以对 'http://www.baidu.com' 网站进行爬取
from urllib.robotparser import RobotFileParser
rp = RobotFileParser()
rp.set_url("http://www.baidu.com/robots.txt")
rp.read()
print(rp.can_fetch('Baiduspider', 'http://www.baidu.com')) 
print(rp.can_fetch('*', 'http://www.baidu.com'))