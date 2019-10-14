import threading
import time
import queue

def consume(thread_name, q):
    while True:
        time.sleep(2)
        product = q.get()
        print("%s consume %s" % (thread_name, product))

def produce(thread_name, q):
    for i in range(3):
        product = 'product-' + str(i)
        q.put(product)
        print("%s produce %s" % (thread_name, product))
        time.sleep(1)
    
            
q = queue.Queue()
p = threading.Thread(target=produce, args=("producer",q))
c = threading.Thread(target=consume, args=("consumer",q))

p.start()
c.start()

p.join()