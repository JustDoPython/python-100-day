import asyncio

async def do_work():
    print("Hello....")
    # 模拟阻塞1秒
    await asyncio.sleep(1)
    print("world...")

coroutine = do_work()
print(coroutine)

# 创建一个事件event_loop
loop = asyncio.get_event_loop()

# 将协程加入到event_loop中，并运行
loop.run_until_complete(coroutine)
