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

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor_test.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
sql = """CREATE TABLE user1 (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor_test.execute(sql)

# 关闭数据库连接
conn.close()