#!/usr/bin/python3
#默认生成0到1之间的随机数
import random
print(random.random())

#uniform(a,b)
import random
print(random.uniform(2,5))
print(random.uniform(5,2))

#randint(a,b)
import random  
print(random.randint(5,50)) 

#randrange([start], stop[, step])
import random
print(random.randrange(1,10))
#print(random.randrange(10,1))
#先从1到10的产生一个间隔是2的等差数列，再从中随机获取一个随机数。
print(random.randrange(1,10,2))

#choice(seq)
import random  
strlist = ['C++','C#','Java','Python']  
strtemp = ('Do you love python')  
print(random.choice(strlist))
print(random.choice(strtemp))  

#shuffle(x[, random])
import random
lst = ['A' , 'B', 'C', 'D', 'E' ]
random.shuffle(lst)  
print (lst)  

#sample(sequence, k)
import random   
lst = [1,2,3,4,5]  
print(random.sample(lst,4))  
print(lst) 
