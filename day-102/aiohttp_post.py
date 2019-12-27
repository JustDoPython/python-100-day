import aiohttp
import asyncio
from datetime import datetime


async def fetch(client):
    data = {'a': '1', 'b': '2'}
    async with client.post('http://httpbin.org/post', data = data) as resp:
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