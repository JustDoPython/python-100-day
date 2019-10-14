import queue
try:
    q = queue.Queue(3)  # 设置队列上限为3
    q.put('python')  # 在队列中插入字符串 'python'
    q.put('-') # 在队列中插入字符串 '-'
    q.put('100') # 在队列中插入字符串 '100'
    q.put('stay hungry, stay foolish', block=False)  # 队列已满，继续往队列中放入数据，引发 queue.Full 异常
except queue.Full:
    print('queue.Full')