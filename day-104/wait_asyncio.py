import asyncio
import time

async def do_work(t):
    print("暂停" + str(t) + "秒")
    # 模拟阻塞1秒
    await asyncio.sleep(t)
    return "暂停了" + str(t) + "秒"


# 任务完成后的回调函数
def callback(future):
    # 打印返回的结果
    print(future.result())


# 创建一个事件event_loop
loop = asyncio.get_event_loop()

tasks = []
i = 0
while i <= 4:
    task = loop.create_task(do_work(i))
    task.add_done_callback(callback)
    tasks.append(task)
    i += 1;


# 计时
now = lambda :time.time()
start = now()
# 将task加入到event_loop中
loop.run_until_complete(asyncio.wait(tasks))

end = now()
print("总共用时间:",end-start)
