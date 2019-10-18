#!/usr/bin/python3
#把json串变成python的数据类型   
import json  
#打开‘users.json’的json文件
f =open('users.json','r',encoding='utf-8')
#读文件
res=f.read()
print(json.loads(res))


#把json串变成python的数据类型：字典，传一个文件对象，不需要再单独读文件 
import json   
#打开文件
f =open('users.json','r',encoding='utf-8') 
print(json.load(f))