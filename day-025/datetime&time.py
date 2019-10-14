#!/usr/bin/python3
#时间戳
import time
print ("当前时间戳为:", time.time())

#函数执行的间隔时间
import time
def calculateTime():
    item = 1
    for i in range(1,100000):
        item = item + i
    return item

startTime = time.time()
result = calculateTime()
endTime = time.time()
print('计算结果：'+ str(result))
print('执行时间：'+ str(endTime - startTime))

#暂停时间
import time
for i in range(2):
    print('one')
    print(time.time())
    time.sleep(1)
    print('two')
    print(time.time())
    time.sleep(1)
print('运行完成')

#当前日期和时间
import datetime
print(datetime.datetime.now())

#获取指定时间
datetest = datetime.datetime(2019,9,30,22,22,0)
print(datetest)
print(str(datetest.year)+"-"+str(datetest.month)+"-"+str(datetest.day)+" "+str(datetest.hour)+":"+str(datetest.minute)+":"+str(datetest.second))

#将时间戳转换成datetime对象
dt1 = datetime.datetime.fromtimestamp(10000)
dt2 = datetime.datetime.fromtimestamp(time.time())

print(dt1)
print(dt2)

#日期转换
datestr = datetime.datetime.strptime('2019-9-30 22:10:00', '%Y-%m-%d %H:%M:%S')
print(datestr)

now = datetime.datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

#日期增加和减少
now = datetime.datetime.now()
print(now)

newdate = now + datetime.timedelta(hours=10)
print(newdate)

newdate = now - datetime.timedelta(days=1)
print(newdate)

