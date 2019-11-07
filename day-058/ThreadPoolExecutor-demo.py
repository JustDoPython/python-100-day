import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

def sayhello(name):
    print("%s say Hello to %s" % (threading.current_thread().getName(), name));
    time.sleep(1)
    return name

name_list =['admin','root','scott','tiger']
start_time = time.time()
with ThreadPoolExecutor(2) as executor: # 创建 ThreadPoolExecutor 
    future_list = [executor.submit(sayhello, name) for name in name_list] # 提交任务

for future in as_completed(future_list):
    result = future.result() # 获取任务结果
    print("%s get result : %s" % (threading.current_thread().getName(), result))

print('%s cost %d second' % (threading.current_thread().getName(), time.time()-start_time))