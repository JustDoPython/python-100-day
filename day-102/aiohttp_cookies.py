import aiohttp
import asyncio
from datetime import datetime


async def fetch(client):
    async with client.get('http://httpbin.org/get') as resp:
        return await resp.text()


async def main():
    cookies = {'cookies': 'this is cookies'}
    async with aiohttp.ClientSession(cookies=cookies) as client:
        html = await fetch(client)
        print(html)

loop = asyncio.get_event_loop()

start = datetime.now()
loop.run_until_complete(main())
end = datetime.now()


print("aiohttp版爬虫花费时间为：")
print(end - start)