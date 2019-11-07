#!/usr/bin/python3
#Pipe管道
from multiprocessing import Process, Pipe
def f(conn):
    conn.send([11, None, 'lily'])
    conn.close()

if __name__ == '__main__':
    conn1, conn2 = Pipe()
    p = Process(target=f, args=(conn2,))
    p.start()
    print(conn1.recv())
    p.join()