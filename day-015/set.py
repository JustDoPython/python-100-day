
set1 = {'hello', 'hello', 'word', 'word'}
print(set1)

# 创建空集合
empty_set = set()

# 创建空字典
empty_dict = {}

# 集合添加元素
s = set(('hello','world'))
print(s)

# 向集合 s 中添加元素
s.add('!')

print('添加元素后的集合是：%s' % s)

# 使用 update() 方法向集合中添加新元素

#　1）添加列表
s.update([1,3],[2,4])
print('添加元素后的集合是：%s' % s)

# 2）添加元组
s.update(('h', 'j'))
print('添加元素后的集合是：%s' % s)

# 移除元素
# 1） remove(x)
s.remove(2)
print('移除元素 2 后的集合是：%s' % s)

# 移除集合中不存在的集合
#s.remove('hi')
#print('移除元素后的集合是：%s' % s)

# discard(x) 此方法移除集合中不存在的元素不会报错
s.discard('hi')
print('移除元素后的集合是：%s' % s)


# 随机删除集合中的一个元素
print(s)

s.pop()

print('移除元素后的集合是：%s' % s)


# 计算集合个数
print('集合 s 的长度是：%s' % len(s))


# 清空集合
s.clear()
print('集合清空后的结果是：%s' % s)


# 判断元素是否存在
s = {'hello',  'word'}
# 判断元素 hello 是否在集合 s 中

print('hello' in s)