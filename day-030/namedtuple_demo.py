from collections import namedtuple
User = namedtuple("User",["name", "age", "weight"])
user = User("admin", 20, 60)
name, age, weight = user

print(user[0])
print(name, age, weight)
print(user.name, user.age, user.weight)

# 常用方法

# 将序列直接转换为新的 tuple 对象
user = ["root", 32, 65]
user = User._make(user) 
print(user)  # User(name='root', age=32, weight=65)

# 返回一个 dict
user = User("admin", 20, 60)
print(user._asdict()) # OrderedDict([('name', 'admin'), ('age', 20), ('weight', 60)])