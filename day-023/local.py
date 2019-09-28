import threading
import time

# 不使用 threading.local
num = 0
def work():
    global num
    for i in range(10):
        num += 1
    print(threading.current_thread().getName(), num)
    time.sleep(0.0001)
for i in range(5):
    threading.Thread(target=work).start()

# 使用 threading.local
num = threading.local()
def work():
    num.x = 0
    for i in range(10):
        num.x += 1
    print(threading.current_thread().getName(), num.x)
    time.sleep(0.0001)
for i in range(5):
    threading.Thread(target=work).start()