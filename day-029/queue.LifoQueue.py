import queue
q = queue.LifoQueue()  # 创建 LifoQueue 队列
for i in range(3):
    q.put(i)  # 在队列中依次插入0、1、2元素
for i in range(3):
    print(q.get())  # 依次从队列中取出插入的元素，数据元素输出顺序为2、1、0