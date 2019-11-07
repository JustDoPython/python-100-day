#!/usr/bin/python3
from multiprocessing import Process
def f(name):
    print('hello', name)
if __name__ == '__main__':
    p = Process(target=f, args=('world',))
    #启动进程
    p.start()
    #实现进程间的同步，等待所有进程退出
    p.join()

#主子进程执行顺序
from multiprocessing import Process
import os
import time
def run():
    print("子进程开启")
    time.sleep(2)
    print("子进程结束")

if __name__ == "__main__":
    print("主进程启动")
    p = Process(target=run)
    p.start()
    print("主进程结束")


