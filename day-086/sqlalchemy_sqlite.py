from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

# 相对路径
engine = create_engine('sqlite:///foo.db', echo=True)

# 绝对路径
# engine = create_engine('sqlite:///C:\\Users\\admin\\Desktop\\db\\foo.db')
# engine = create_engine(r'sqlite:///C:\Users\admin\Desktop\db\foo.db')

# 内存数据库
# engine = create_engine('sqlite://', echo=True)
# conn = engine.connect()

# 映射基类
Base = declarative_base()

# 具体映射类
class SysUser(Base):
    # 指定映射表名
    __tablename__ = 'sys_user'

    # id 设置为主键
    id = Column(Integer, primary_key=True)
    # 指定 name 映射到 name 字段
    name = Column(String(30))
    password = Column(String(32))

# 创建表
# Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
# 创建 Session 类实例
session = Session()

# 新增
# su = SysUser(id=1, name='Jhon', password='123456')
# 保存
# session.add(su)
# 提交
# session.commit()
# 关闭
# session.close()

# 查询
# u = session.query(SysUser).filter(SysUser.id==1).one()
# session.query(SysUser).filter(SysUser.id==1).all()
# print('name-->',u.name)
# session.close()

# 修改
# u = session.query(SysUser).filter(SysUser.id==1).one()
# print('修改前名字-->', u.name)
# u.name = 'James'
# session.commit()
# print('修改后名字-->', u.name)
# session.close()

# 删除
u = session.query(SysUser).filter(SysUser.id==1).one()
session.delete(u)
session.commit()
session.close()