#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""

import socket
import threading
import time


# 处理tcp连接
def tcplink(conn, addr):
    print("Accept new connection from %s:%s" % addr)
    # 向客户端发送欢迎消息
    conn.send(b"Server: Welcome!\n")
    while True:
        conn.send(b"Server: What's your name?")

        data = conn.recv(1024)
        # 如果客户端发送 exit 过来请求退出，结束循环
        if data == b"exit":
            conn.send(b"Server: Good bye!\n")
            break
        conn.send(b"Server: Hello %s!\n" % data)

    time.sleep(5)
    # 关闭连接
    conn.close()
    print("Connection from %s:%s is closed" % addr)


# 创建 socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口
s.bind(("127.0.0.1", 6000))
# 设定等待连接的最大数量为5
s.listen(5)
print("Waiting for connection...")
# 等待接收连接
while True:
    # 接受一个新连接
    conn, addr = s.accept()
    # 创建新线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(conn, addr))
    t.start()
