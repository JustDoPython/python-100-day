dict = {'Name': 'Mary', 'Age': 20,'Address':'BeiJing'}

# 检测键 Age 是否存在
if 'Age' in dict:
    print("键 Age 存在")
else:
    print("键 Age 不存在")

# 检测键 Sex 是否存在
if 'Sex' in dict:
    print("键 Sex 存在")
else:
    print("键 Sex 不存在")

# not in

# 检测键 Name 是否存在
if 'Name' not in dict:
    print("键 Name 不存在")
else:
    print("键 Name 存在")