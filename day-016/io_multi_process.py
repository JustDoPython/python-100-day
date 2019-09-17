# I/O 密集型任务-多进程
from multiprocessing import Process
import os,time

def task():
    f = open('tmp.txt','w')
if __name__ == '__main__':
    arr = []
    print('本机为',os.cpu_count(),'核 CPU')
    start = time.time()
    for i in range(500):
        p = Process(target=task)
        arr.append(p)
        p.start()
    for p in arr:
        p.join()
    stop = time.time()
    print('I/O 密集型任务，多进程耗时 %s' % (stop - start))