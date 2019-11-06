import queue
q = queue.Queue()
q.put(100)
q.put(200)
q.qsize() # 获取队列大小，此处结果为 2


import queue
q = queue.Queue(maxsize=1)
q.empty() # 判断队列是否空，此处结果为 True
q.full() # 判断队列是否满，此处结果为 False
q.put(100)
q.empty() # False
q.full() # True