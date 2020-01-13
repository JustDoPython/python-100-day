import asyncio
import functools


async def do_work(t):
    print("暂停" + str(t) + "秒")
    await asyncio.sleep(t)
    return "暂停了" + str(t) + "秒"


def callback(loop, gatheringFuture):
    print(gatheringFuture)
    print("多个Task任务完成后的回调")
    loop.stop()


loop = asyncio.get_event_loop()

gather = asyncio.gather(do_work(1), do_work(3))
gather.add_done_callback(functools.partial(callback, loop))

loop.run_forever()
