
dict = {'Name': 'Mary', 'Age': 17}

print("Value : %s" % dict.items())


#　可遍历实例
dict1 = {'老大':'15岁',
        '老二':'14岁',
        '老三':'2岁',
        }
print(dict1.items())
for key,values in dict1.items():
    print(key + '已经' + values + '了')


