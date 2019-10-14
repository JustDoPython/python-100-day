import queue
q = queue.PriorityQueue()  # 创建 PriorityQueue 队列
data1 = (1, 'python')
data2 = (2, '-')
data3 = (3, '100')
style = (data2, data3, data1)
for i in style:
    q.put(i)  # 在队列中依次插入元素 data2、data3、data1
for i in range(3):
    print(q.get())  # 依次从队列中取出插入的元素，数据元素输出顺序为 data1、data2、data3