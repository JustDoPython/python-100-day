#!/usr/bin/python3
# dumps功能
import pickle
data = ['A', 'B', 'C','D']  
datastr = pickle.dumps(data)
print(datastr)


# dump功能
with open('test.txt', 'wb') as f:
    pickle.dump(data, f)
print('写入成功')


# loads功能
msg = pickle.loads(datastr)
print(msg)


# load功能
with open('test.txt', 'rb') as f:
   data = pickle.load(f)
print(data)