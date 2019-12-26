import asyncio


async def do_work():
    print("这是一个Task例子....")
    # 模拟阻塞1秒
    await asyncio.sleep(1)
    return "Task任务完成"

# 创建一个事件event_loop
loop = asyncio.get_event_loop()

# 创建一个task
task = loop.create_task(do_work())
# 第一次打印task
print(task)

# 将task加入到event_loop中
loop.run_until_complete(task)
# 再次打印task
print(task)
print(task.result())
