s = '学习Python'
# 切片
s[0], s[-1], s[3:], s[::-1]	# '优', 'n', 'Python', 'nohtyP的雅优'
# 替换，还可以使用正则表达式替换
s.replace('Python', 'Java')	# '学习Java'
# 查找，find()、index()、rfind()、rindex()
s.find('P')			# 3, 返回第一次出现的子串的下标
s.find('h', 2)			# 6, 设定下标2开始查找
s.find('23333')			# -1, 查找不到返回-1
s.index('y')			# 4, 返回第一次出现的子串的下标
s.index('P')		# 不同与find(), 查找不到会抛出异常
# 转大小写, upper()、lower()、swapcase()、capitalize()、istitle()、isupper()、islower()
s.upper()			# '学习PYTHON'
s.swapcase()			# '学习pYTHON', 大小写互换
s.istitle()			# True
s.islower()			# False
# 去空格,strip()、lstrip()、rstrip()
# 格式化
s1 = '%s %s' % ('Windrivder', 21)	# 'Windrivder 21' 
s2 = '{}, {}'.format(21, 'Windridver')	# 推荐使用format格式化字符串
s3 = '{0}, {1}, {0}'.format('Windrivder', 21)
s4 = '{name}: {age}'.format(age=21, name='Windrivder')
# 连接与分割，使用 + 连接字符串，每次操作会重新计算、开辟、释放内存，效率很低，所以推荐使用join
l = ['2017', '03', '29', '22:00']
s5 = '-'.join(l)			# '2017-03-29-22:00'
s6 = s5.split('-')			# ['2017', '03', '29', '22:00']

# encode 将字符转换为字节
str = '学习Python'      
print (str.encode())			# 默认编码是 UTF-8  输出：b'\xe5\xad\xa6\xe4\xb9\xa0Python'
print (str.encode('gbk'))      # 输出  b'\xd1\xa7\xcf\xb0Python'
# decode 将字节转换为字符
print (str.encode().decode('utf8'))   # 输出 '学习Python'
print (str.encode('gbk').decode('gbk'))             # 输出 '学习Python'
