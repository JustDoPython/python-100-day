import queue
try:
    q = queue.Queue(2)  # 设置队列上限为2
    q.put('python')  # 在队列中插入字符串 'python'
    q.put('-') # 在队列中插入字符串 '-'
    q.put('100', block = True, timeout = 5) # 队列已满，继续在队列中插入字符串 '100'，等待5秒后会引发 queue.Full 异常
except queue.Full:
    print('queue.Full')