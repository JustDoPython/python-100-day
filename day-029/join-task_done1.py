import queue
q = queue.Queue()
q.put('python')
q.put('-')
q.put('100')
for i in range(3):
    print(q.get())
    q.task_done()  # 如果不执行 task_done，join 会一直处于阻塞状态，等待 task_done 告知它数据的处理已经完成
q.join()

