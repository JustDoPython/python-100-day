
# dict.fromkeys(seq[, value])
seq = ('name', 'age', 'class')

#
dict = dict.fromkeys(seq)
print("新的字典为 : %s" % str(dict))

dict = dict.fromkeys(seq, 10)
print("新的字典为 : %s" % str(dict))

dict = dict.fromkeys(seq,('zs',8,'Two'))
print("新的字典为 : %s" % str(dict))