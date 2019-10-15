import queue
try:
    q = queue.Queue()
    q.get_nowait() # 队列为空，往队列中取数据时直接引发 queue.Empty 异常
except queue.Empty:
    print('queue.Empty')