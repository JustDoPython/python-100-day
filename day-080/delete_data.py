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

sql = "DELETE * FROM user1"

try:
    # 执行SQL语句
    cursor_test.execute(sql)
    # 提交到数据库执行
    conn.commit()
except:
    # 发生错误时回滚
    conn.rollback()

# 关闭数据库连接
conn.close()