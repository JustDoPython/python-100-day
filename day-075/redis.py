import redis   #导入redis模块

# 建议使用以下连接池的方式
# 设置decode_responses=True，写入的KV对中的V为string类型，不加则写入的为字节类型。
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, decode_responses=True)
rs = redis.Redis(connection_pool=pool)

# key="color",value="red"，设置过期时间5秒
rs.set('color', 'red', ex=5)

# 与rs.set('color', 'red', ex=5)相同
rs.setex('color', 5, 'red')

# 打印获取color键对应的值，超时后获取值为None
print(rs.get('color'))

# 如果color存在输出None，如果不存在，则输出True
print(rs.set('color', 'green', nx=True))

# 如果color存在输出True，如果不存在，则输出None
print(rs.set('color', 'yellow', xx=True))



# 批量赋值
rs.mset({'key1':'value1', 'key2':'value2', 'key3':'value3'})

# 批量获取值
rs.mget('key1', 'key2', 'key3')



# 设置新值为blue，同时返回设置前的值
print(rs.getset('color', 'blue'))  

rs.set('lang', 'Chinese')

# 取索引为1-3字符
print(rs.getrange('lang', 1, 3))  #返回结果： hin

# 从索引号为4字符开始向后替换
rs.setrange('lang', 4, 'a is great')   #返回结果：14

# 在lang对应值后面追加字符 "!"
rs.append('lang', '!')         #返回结果： 15

print(rs.get('lang'))    #返回结果：China is great!

# 返回lang对应值的长度
print(rs.strlen('lang'))   #返回结果：15

# 如果total对应值不存在，则total当前值设置为10
rs.incr('total', amount=10)

# 当前total对应值增加1
rs.incr('total')    #结果为11

# 当前total对应值减少1
rs.decr('total')    #结果为10



# 每个新增元素都插入到list最左边，如果list不存在则会新建
rs.lpush('leftList', 1,2,3,4,5)
print(rs.lrange('leftList', 0, -1))  #返回结果：['5', '4', '3', '2', '1']

# 新插入元素在右侧，如果list不存在则新建
rs.rpush('rightList', 6,7,8,9,10)
print(rs.lrange('rightList', 0, -1))   #返回结果：['6', '7', '8', '9', '10']

# 在list左边新增元素，如果list不存在则不创建
rs.lpushx('noList', 'apple')
print(rs.llen('noList'))     #返回结果：0

# 在list中从左遍历出第一个为'7'的元素，在它后面(如果是在前面插入则用'before')插入元素'08'
rs.linsert('rightList', 'after', '7', '08')  
print(rs.lrange('rightList', 0, -1))   #返回结果：['6', '7', '08', '8', '9', '10']

# 将list中索引号为1的元素修改为'-7'
rs.lset('rightList', 1, '-7')
print(rs.lrange('rightList', 0, -1))   #返回结果：['6', '-7', '08', '8', '9', '10']

# 删除list中从左遍历第一个为'8'的元素
rs.lrem('rightList', '8', 1)
print(rs.lrange('rightList', 0, -1))   #返回结果：['6', '-7', '08', '9', '10']

# 弹出左侧第一个元素
rs.lpop('rightList')       #返回值为：'6'
print(rs.lrange('rightList', 0, -1))   #返回结果：['-7', '08', '9', '10']

#取出list中索引编号为1的值
print(rs.lindex('rightList', 1))  #返回结果：08




# 单键值操作
# 设置hash名为hName的键和值
rs.hset('hName', 'key1', 'value1')
rs.hset('hName', 'key2', 'value2')

# 取hName的key1对应的值
print(rs.hget('hName', 'key1'))   #返回结果：value1

#批量键值操作
rs.hmset('hName', {'key3': 'value3', 'key5': 'value5'})
print(rs.hmget('hName', 'key1', 'key2', 'key3'))  #返回结果：['value1', 'value2', 'value3']

# 取出hName所有键值
print(rs.hgetall('hName'))  #返回结果：{'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key5': 'value5'}

# 取hName中所有的keys
print(rs.hkeys('hName'))  #返回结果：['key1', 'key2', 'key3', 'key5']

# 取hName中所有的values
print(rs.hvals('hName'))  #返回结果：['value1', 'value2', 'value3', 'value5']

# 获取hName对应hash键值对个数
print(rs.hlen('hName'))   #返回结果：4

# 判断key2是否存在
print(rs.hexists('hName', 'key2'))   #返回结果：True

# 删除key2对应键值对
rs.hdel('hName', 'key2')

# 再次判断key2是否存在
print(rs.hexists('hName', 'key2'))   #返回结果：False







# 增加集合元素，如集合不存在则新建
rs.sadd('mySet', 'one', 'two', 3)

# 返回集合元素个数
print(rs.scard('mySet'))

# 返回所有元素
print(rs.smembers('mySet'))    #结果：{'two', 'one', '3'}

# 返回所有成员
print(rs.sscan('mySet'))   #结果：(0, ['3', 'one', 'two'])

# 再次创建一个集合mySet2
rs.sadd('mySet2', 3, 5, 7)

# 获取两个集合交集
print(rs.sinter('mySet', 'mySet2'))    #返回结果：{'3'}

# 获取两个集合并集
print(rs.sunion('mySet', 'mySet2'))   #返回结果：{'5', 'two', 'one', '7', '3'}

# 获取两个集合差集
print(rs.sdiff('mySet', 'mySet2'))   #返回结果：{'two', 'one'}

# 取mySet和mySet2的并集，将结果存到storeSet集合中
print(rs.sunionstore('sotreSet', 'mySet', 'mySet2'))
print(rs.smembers('sotreSet'))    #返回结果：{'5', 'two', 'one', '7', '3'}

# 判断one元素是否存在集合中
print(rs.sismember('sotreSet', 'one'))

# 随机删除并返回集合中的一个元素
print(rs.spop('sotreSet'))

# 删除集合中元素值为5的元素
print(rs.srem('sotreSet', 5))





# 增加集合元素，如集合不存在则新建
rs.zadd('fruits', {'apple':1, 'banana':3, 'orange':5})

# 遍历所有元素
print(rs.zrange("fruits", 0, -1))    #结果：['apple', 'banana', 'orange']

# withscores=True指带上分数
print(rs.zrange("fruits", 0, -1, withscores=True))   #结果：[('apple', 1.0), ('banana', 3.0), ('orange', 5.0)]

# 根据分数由大到小遍历所有元素
print(rs.zrevrange("fruits", 0, -1))   #结果：['orange', 'banana', 'apple']

# 获取orange元素对应的分数
rs.zscore('fruits', 'orange')     #结果：5.0

# 取出分数>=3 and 分数<=5的元素
print(rs.zrangebyscore('fruits', 3, 5))

# 取出分数<=5 and 分数>=3的元素，根据分数从大到小排序
print(rs.zrevrangebyscore('fruits', 5, 3))

# 遍历所有元素，返回一个元组
print(rs.zscan('fruits'))   #结果：(0, [('apple', 1.0), ('banana', 3.0), ('orange', 5.0)])

# 打印集合元素个数
print(rs.zcard('fruits'))    #结果：3

# 返回集合中分数>=1 and 分数<=3元素个数
print(rs.zcount('fruits', 1, 3))

# 将集合中apple元素的分数+5
rs.zincrby('fruits', 5, 'apple')
print(rs.zrange("fruits", 0, -1, withscores=True))   #返回结果：[('banana', 3.0), ('orange', 5.0), ('apple', 6.0)]

# 返回orange元素在集合中的索引号
rs.zrank('fruits', 'orange')     #结果：1

# 按分数从大到小排序，取出banana元素索引号
rs.zrevrank('fruits', 'banana')   #结果：2

# #删除集合中apple元素
rs.zrem('fruits', 'apple')
print(rs.zrange("fruits", 0, -1))   #返回结果：['banana', 'orange']

# #删除集合索引号>=0 and 索引号<=2的元素
rs.zremrangebyrank('fruits', 0, 2)

# 删除集合分数>=1 and 分数<=5的元素
rs.zremrangebyscore('fruits', 1, 5)









# 删除key为color的对象
rs.delete('color')

# 查询key为color的对象是否存在
print(rs.exists('color'))    #结果：False
rs.sadd('mySet5', 'one', 'two')

# 设置key的超时时间
rs.expire('mySet5', time=5)   #单位：秒

# 重命名key的值
rs.rename('mySet5', 'set5')

# 随机返回当前库中一个key，但不会删除
print(rs.randomkey())

# 查看某个key对应值的类型
print(rs.type('mySet'))   #返回结果：set

# 通过模糊匹配出满足条件的key
print(rs.keys('my*'))    #返回结果：['mySet', 'mySet2']

#各类型元素迭代方式
#hash类型迭代
for i in rs.hscan_iter("hName"):
    print(i)

#set类型迭代
for j in rs.sscan_iter("mySet"):
    print(j)

#zset类型迭代
for k in rs.zscan_iter("fruits"):
    print(k)
