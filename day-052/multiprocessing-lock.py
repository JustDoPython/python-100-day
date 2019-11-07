#!/usr/bin/python3
from multiprocessing import Process, Lock
def f(l, i):
    l.acquire()
    try:
        print('this is', i)
    finally:
        l.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()