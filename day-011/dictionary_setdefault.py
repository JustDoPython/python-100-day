dict = {'Name': 'Mary', 'Age': 17}

print("Age 键的值为 : %s" % dict.setdefault('Age', None))
print("Sex 键的值为 : %s" % dict.setdefault('Sex', None))
print("新字典为：", dict)
