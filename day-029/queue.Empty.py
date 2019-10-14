import queue
try:
    q = queue.Queue(3)  # 设置队列上限为3
    q.put('python')  # 在队列中插入字符串 'python'
    q.put('-') # 在队列中插入字符串 '-'
    q.put('100') # 在队列中插入字符串 '100'
    for i in range(4):  # 从队列中取数据，取出次数为4次，引发 queue.Empty 异常
        print(q.get(block=False))
except queue.Empty:
    print('queue.Empty')