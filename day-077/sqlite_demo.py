# 导入模块
import sqlite3

# 连接数据库
conn = sqlite3.connect('test.db')

# 创建游标
cs = conn.cursor()

# 创建表
# cs.execute('''CREATE TABLE student
#        (id varchar(20) PRIMARY KEY,
#         name varchar(20));''')
# 关闭 Cursor
# cs.close()
# 提交
# conn.commit()
# 关闭连接
# conn.close()

# 新增
# cs.execute("INSERT INTO student (id, name) VALUES ('1', 'Jhon')")
# cs.execute("INSERT INTO student (id, name) VALUES ('2', 'Alan')")
# cs.close()
# conn.commit()
# conn.close()

# 查询
# cs.execute("SELECT id, name FROM student")
# data = cs.fetchall()
# print(data)
# cs.close()
# conn.close()

# 修改
# cs.execute("SELECT id, name FROM student WHERE id = '1'")
# print('修改前-->', cs.fetchall())
# cs.execute("UPDATE student set name = 'Nicolas' WHERE id = '1'")
# cs.execute("SELECT id, name FROM student WHERE id = '1'")
# print('修改后-->', cs.fetchall())
# conn.commit()
# cs.close()
# conn.close()

# 删除
# cs.execute("SELECT id, name FROM student")
# print('删除前-->', cs.fetchall())
# cs.execute("DELETE FROM student WHERE id = '1'")
# cs.execute("SELECT id, name FROM student")
# print('删除后-->', cs.fetchall())
# conn.commit()
# cs.close()
# conn.close()