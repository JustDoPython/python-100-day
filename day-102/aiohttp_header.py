import aiohttp
import asyncio
from datetime import datetime


async def fetch(client):
    headers = {'content-type': 'application/json', 'User-Agent': 'Python/3.8 aiohttp/3.8.2'}
    async with client.get('http://httpbin.org/get',headers=headers) as resp:
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