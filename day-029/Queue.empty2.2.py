import queue
q = queue.Queue()
print(q.empty())  # 对列为空，返回 True
q.put('python-100')  # 在队列中插入元素 'python-100'
print(q.empty())  # 对列不为空，返回 False