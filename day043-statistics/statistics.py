#计算平均数
>>> statistics.mean([1, 2, 3, 4, 5])

>>> from fractions import Fraction as F
>>> statistics.mean([F(4, 7), F(4, 21), F(5, 4), F(1, 4)])

>>> from decimal import Decimal as D
>>> statistics.mean([D("0.5"), D("0.78"), D("0.88"), D("0.988")])


#计算调和平均数
>>> statistics.harmonic_mean([4, 5, 7])


#计算中值
>>> statistics.median([1, 4, 7])

>>> statistics.median([1, 4, 7, 10])


#计算中小值
>>> statistics.median_low([1, 4, 7])

>>> statistics.median_low([1, 4, 7, 10])


#计算中大值
>>> statistics.median_high([1, 4, 7])

>>> statistics.median_high([1, 4, 7, 10])


#计算中位数
>>> statistics.median_grouped([1, 2, 2, 3, 4, 4, 4, 4, 4, 5])

>>> statistics.median_grouped([3, 4, 4, 5, 6], interval=1)

>>> statistics.median_grouped([1, 3, 5, 5, 7], interval=2)


#计算众数
>>> statistics.mode([1, 1, 2, 3, 3, 3, 3, 4])

>>> statistics.mode(["red", "blue", "blue", "blue", "green", "green", "red"])
