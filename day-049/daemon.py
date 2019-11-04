import threading
def work(num):
    for i in range(num):
        print(threading.current_thread().name + "  " + str(i))
t = threading.Thread(target=work, args=(10,), name='守护线程')
#t.daemon = True
t.start()
for i in range(10):
    pass