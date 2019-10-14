import queue
q = queue.Queue(3)  # 定义一个长度为3的队列
print(q.full())  # 元素个数未达到上限，返回 False
q.put('python')  # 在队列中插入字符串 'python'
q.put('-') # 在队列中插入字符串 '-'
q.put('100') # 在队列中插入字符串 '100'
print(q.full())  # 元素个数达到上限，返回 True