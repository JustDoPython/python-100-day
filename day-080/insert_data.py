import pymysql

# 打开数据库连接
conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="123456",
    database="test_db",
    charset="utf8")

# 获取连接下的游标
cursor_test = conn.cursor()

# 使用预处理语句创建表
sql = """INSERT INTO user1(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Fei', 'Fei', 20, 'M', 1000)"""

try:
   # 执行sql语句
   cursor_test.execute(sql)
   # 提交到数据库执行
   conn.commit()
except:
   # 如果发生错误则回滚
   conn.rollback()

# 关闭数据库连接
conn.close()