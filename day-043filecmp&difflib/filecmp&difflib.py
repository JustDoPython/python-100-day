#新建两个文件f1 和 f2
#f1存储的数据是1,2,3
#f2存储的数据是4,5,6
import filecmp
print(filecmp.cmp("f1","f1"))
print(filecmp.cmp("f1","f2"))


import difflib
from pprint import pprint

a = 'pythonclub.org is wonderful'
b = 'Pythonclub.org also wonderful'
s = difflib.SequenceMatcher(None, a, b)

print ("s.get_matching_blocks():")
pprint(s.get_matching_blocks())
print ("s.get_opcodes():")
for tag, i1, i2, j1, j2 in s.get_opcodes():
    print ("%7s a[%d:%d] (%s) b[%d:%d] (%s)" %  (tag, i1, i2, a[i1:i2], j1, j2, b[j1:j2]))
    
