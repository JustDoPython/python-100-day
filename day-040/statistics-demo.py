import statistics

example_list = [1,2,3,4,5,6]

x = statistics.mean(example_list)
print(x)

x = statistics.harmonic_mean(example_list)
print(x)
print(1/sum([1/1,1/2,1/3,1/4,1/5,1/6])*6)

x = statistics.median(example_list)
print(x)

x = statistics.median_low(example_list)
print(x)

x = statistics.median_high(example_list)
print(x)

x = statistics.mode([1,1,2,3,4,3,3,3,3])
print(x)

x = statistics.mode(["a","b","c","d","d","a","a",])
print(x)

x = statistics.pstdev([2,2,2,6])
print(x)

x = statistics.pvariance([2,2,2,6])
print(x)

x = statistics.stdev([2,2,2,6])
print(x)

x = statistics.variance([2,2,2,6])
print(x)
