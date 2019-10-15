import queue
try:
    q = queue.Queue()
    q.get(block = True, timeout = 5) # 队列为空，往队列中取数据时，等待5秒后会引发 queue.Empty 异常
except queue.Empty:
    print('queue.Empty')