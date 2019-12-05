# 导入模块
import pymysql

# 打开数据库连接
conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="123456",
    database="test_db",
    charset="utf8")
# print(conn)
# print(type(conn))

# 获取连接下的游标
cursor_test = conn.cursor()
# print(cursor_test)

# 使用 execute()  方法执行 SQL 查询，查询数据库版本
cursor_test.execute("SELECT VERSION()")

# 使用 fetchone() 方法返回一条数据.
data = cursor_test.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
conn.close()

