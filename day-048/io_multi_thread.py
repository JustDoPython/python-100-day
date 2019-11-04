# I/O 密集型任务-多线程
from threading import Thread
import os,time

def task():
    f = open('tmp.txt','w')
if __name__ == '__main__':
    arr = []
    print('本机为',os.cpu_count(),'核 CPU')
    start = time.time()
    for i in range(500):
        p = Thread(target=task)
        arr.append(p)
        p.start()
    for p in arr:
        p.join()
    stop = time.time()
    print('I/O 密集型任务，多线程耗时 %s' % (stop - start))