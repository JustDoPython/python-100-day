# 计算密集型任务-单线程
from threading import Thread
import os,time

def task():
    ret = 0
    for i in range(100000000):
        ret *= i
if __name__ == '__main__':
    print('本机为',os.cpu_count(),'核 CPU')
    start = time.time()
    for i in range(5):
        task()
    stop = time.time()
    print('单线程耗时 %s' % (stop - start))