#!/usr/bin/python3
#Pipe管道
from multiprocessing import Process, Pipe
def f(conn):
    conn.send([11, None, 'lily'])
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()