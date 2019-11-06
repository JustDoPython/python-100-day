import time
import threadpool
import threading

def sayhello(name):
    print("%s say Hello to %s" % (threading.current_thread().getName(), name));
    time.sleep(1)
    return name

def callback(request, result): # 回调函数，用于取回结果
    print("callback result = %s" % result)

name_list =['admin','root','scott','tiger']
start_time = time.time()
pool = threadpool.ThreadPool(2) # 创建线程池
requests = threadpool.makeRequests(sayhello, name_list, callback) # 创建任务
[pool.putRequest(req) for req in requests] # 加入任务
pool.wait() 
print('%s cost %d second' % (threading.current_thread().getName(), time.time()-start_time))