import aiohttp
import asyncio
from datetime import datetime


async def fetch(client):
    #params = {"a": 1,"b": 2}
    #params = [('a', 1), ('b', 2)]
    async with client.get('http://httpbin.org/get',params='q=aiohttp+python&a=1') as resp:
        return await resp.text()


async def main():
    async with aiohttp.ClientSession() as client:
        html = await fetch(client)
        print(html)

loop = asyncio.get_event_loop()

start = datetime.now()
loop.run_until_complete(main())
end = datetime.now()


print("aiohttp版爬虫花费时间为：")
print(end - start)