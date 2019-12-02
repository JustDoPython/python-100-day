#导入 MongoClient 模块
from pymongo import MongoClient, ASCENDING, DESCENDING

# 两种方式
#1. 传入数据库IP和端口号
mc = MongoClient('127.0.0.1', 27017)

#2. 直接传入连接字串
mc = MongoClient('mongodb://127.0.0.1:27017')

# 有密码的连接
# 首先指定连接testdb数据库
# db = mc.testdb

# 通过authenticate方法认证账号密码
# db.authenticate('username','password')

# 检查是否连接成功，输出以下结果表示连接成功
print(mc.server_info())


# 指定操作数据库的两种方式
#1. 获取 testdb 数据库，没有则自动创建
db = mc.testdb

#2. 效果与上面 db = mc.testdb 相同
db = mc['testdb']

# 打印出testdb数据库下所有集合(表)
print(db.collection_names())


# 指定操作集合的两种方式
#1. 获取 test 集合，没有则自动创建
collection = db.test

#2. 效果与 collection = db.test 相同
collection = db['test']

# 打印集合中一行数据
print(collection.find_one())



book = {
      'name' : 'Python基础',
      'author' : '张三',
      'page' : 80
}

# 向集合中插入一条记录
collection.insert_one(book)

# 对于insert_many()方法，我们可以将数据以列表形式传递参数
book1 = {
      'name' : 'Java基础',
      'author' : '李白',
      'page' : 100
}
book2 = {
      'name' : 'Java虚拟机',
      'author' : '王五',
      'page' : 100
}

# 创建 book_list 列表
book_list = [book1, book2]

# 向集合中插入多条记录
collection.insert_many(book_list)


# 通过条件查询一条记录，如果不存在则返回None
res = collection.find_one({'author': '张三'})
print (res)

# 通过条件查询多条记录，如果不存在则返回None
res = collection.find({'page': 100})
print (res)

# 使用 find() 查询会返回一个对象
# 遍历对象，并打印查询结果
for r in res:
   print(r)

# 查询page大于50的记录
res = collection.find({'page': {'$gt': 50}})



book = collection.find_one({'author': '张三'})
book['page'] = 90

# 更新满足条件{'author', '张三'}的第一条记录
res = collection.update_one({'author': '张三'}, {'$set': book})

# 更新返回结果是一个对象，我们可以调用matched_count和modified_count属性分别获得匹配的数据条数和影响的数据条数。
print(res.matched_count, res.modified_count)

# 更新满足条件 page>90 的所有记录，page 字段自加 10
res = collection.update_many({'page': {'$gt': 90}}, {'$inc': {'page': 10}})

# 打印更新匹配和影响的记录数
print(res.matched_count, res.modified_count)

book3 = {'name':'Python高级', 'author':'赵飞', 'page': 50}

#upsert=True表示如果没有满足更新条件的记录，则会将book3插入集合中
res = collection.update_one({'author': '赵飞'}, {'$set': book3}, upsert=True)
print(res.matched_count, res.modified_count)

# 查询所有记录，并遍历打印出来
res = collection.find()
for r in res:
   print(r)



# 删除满足条件的第一条记录
result = collection.delete_one({'author': '张三'})
# 同样可以通过返回对象的 deleted_count 属性查询删除的记录数
print(result.deleted_count)

# 删除满足条件的所有记录，以下为删除 page < 90 的记录
result = collection.delete_many({'page': {'$lt': 90}})
print(result.deleted_count)



# 查询返回满足条件的记录然后删除
result = collection.find_one_and_delete({'author': '王五'})  
print(result)

# 统计查询结果个数
# 全部结果个数
collection.find().count()

# 满足条件结果个数
collection.find({'page': 100}).count()

# 查询结果按字段排序
# 升序
results = collection.find().sort('page', ASCENDING)

# 降序
results = collection.find().sort('page', DESCENDING)

# 下面查询结果是按page升序排序，只返回第二条记录及以后的两条结果
results = collection.find().sort('page', ASCENDING).skip(1).limit(2)
print(results)




# unique=True时，创建一个唯一索引，索引字段插入相同值时会自动报错，默认为False
collection.create_index('page', unique= True)

# 打印出已创建的索引
print(collection.index_information())

# 删除索引
collection.drop_index('page_1')

#删除集合
collection.drop()

