import itertools
def sortBy(score):
	if score > 80:
		return "A"
	elif score >= 60:
		return "B"
	else:
		return "C"

scores = [81, 82, 84, 76, 64, 78, 59, 44, 55, 89]
#scores = sorted(scores, key=sortBy) # 将此行代码注释打开即可得到合理的结果
for m, n in itertools.groupby(scores, key=sortBy):
	print(m, list(n))
