#!/usr/bin/python3
#Queue队列
from multiprocessing import Process, Queue
def f(q):
    q.put([11, None, 'lily'])
if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())
    p.join()