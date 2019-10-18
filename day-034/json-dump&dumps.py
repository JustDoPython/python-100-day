#!/usr/bin/python3
#字典转成json字符串 加上ensure_ascii=False以后，可以识别中文， indent=4是间隔4个空格显示             
import json                                                                                         
d={'小明':{'sex':'男','addr':'上海','age':26},'小红':{ 'sex':'女','addr':'上海', 'age':24},}
print(json.dumps(d,ensure_ascii=False,indent=4)) 


#字典转成json字符串,不需要写文件，自动转成的json字符串写入到‘users.json’的文件中 
import json                                                                         
d={'小明':{'sex':'男','addr':'上海','age':26},'小红':{ 'sex':'女','addr':'上海', 'age':24},}
#打开一个名字为‘users.json’的空文件
fw =open('users.json','w',encoding='utf-8')

json.dump(d,fw,ensure_ascii=False,indent=4)
print('保存成功')
