from MyQR import myqr

'''
words：内容
version：容错率
save_name：保存的名字
'''
# myqr.run(words='https://www.baidu.com/',
#          version=1,
# 	     save_name='myqr.png')

'''
picture：生成二维码用到的图片
colorized：False 为黑白，True 为彩色
'''
# myqr.run(words='https://www.baidu.com/',
#          version=1,
#          picture='bg.jpg',
#          colorized=True,
# 	       save_name='pmyqr.png')

myqr.run(words='https://www.baidu.com/',
         version=1,
         picture='my.gif',
         colorized=True,
	     save_name='myqr.gif')
