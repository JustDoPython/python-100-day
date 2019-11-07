import queue
q = queue.Queue(maxsize=1)
q.put(100)


import queue
q = queue.Queue(maxsize=1)
q.put(100)
q.put(100,True,2) # 创建一个容量为 1 的队列，2 秒内没有位置添加任务则引发 Full 异常
q.put(100) # 该方法会一直阻塞


import queue
q = queue.Queue(maxsize=1)
q.put(100)
q.put(100,False,2) # 创建一个容量为 1 的队列，在第二次放入任务时指定为非阻塞模式，则会立刻引发 Full 异常


import queue
q = queue.Queue()
q.put(100)
q.get() # 此处的返回值为 100。交互模式下才会有输出，如果用 idea 请使用 print(q.get()) 查看结果（下同）

import queue
q = queue.Queue()
q.put(100)
q.get() # 此处的返回值为 100
q.get(True,2) # 2 秒钟内没有任务可获取，则引发 Empty 异常
q.get() # 因为队列为空，所以该方法会一直阻塞


import queue
q = queue.Queue()
q.put(100)
q.get() # 此处的返回值为 100
q.get(False,2) # 指定为非阻塞模式，队列为空则立即引发 Empty 异常
