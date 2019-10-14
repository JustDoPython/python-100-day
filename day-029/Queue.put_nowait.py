import queue
try:
    q = queue.Queue(2)  # 设置队列上限为2
    q.put_nowait('python')  # 在队列中插入字符串 'python'
    q.put_nowait('-') # 在队列中插入字符串 '-'
    q.put_nowait('100') # 队列已满，继续在队列中插入字符串 '100'，直接引发 queue.Full 异常
except queue.Full:
    print('queue.Full')