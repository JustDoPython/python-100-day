import asyncio

async def do_work():
    print("这是一个Task例子....")
    # 模拟阻塞1秒
    await asyncio.sleep(1)
    return "Task任务完成"

# 任务完成后的回调函数
def callback(task):
    # 打印参数
    print(task)
    # 打印返回的结果
    print(task.result())

# 创建一个事件event_loop
loop = asyncio.get_event_loop()

# 创建一个task
task = loop.create_task(do_work())
task.add_done_callback(callback)

# 将task加入到event_loop中
loop.run_until_complete(task)
