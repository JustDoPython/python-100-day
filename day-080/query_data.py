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

sql = """
    select * from user1"""

try:
    # 执行 sql 语句
    cursor_test.execute(sql)
    # 显示出所有数据
    data_result = cursor_test.fetchall()
    for row in data_result:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
              (fname, lname, age, sex, income))
except:
    print("Error: unable to fetch data")

# 关闭数据库连接
conn.close()

