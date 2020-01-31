'''
__author__ = justdopython.com
'''


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter


# 生成所要用到的数据集
def getData() -> (np.ndarray, np.ndarray, np.ndarray, np.ndarray):
    iris = pd.read_csv('iris.csv').to_numpy()
    train_data = [] # 训练数据，与测试数据按 4:1 比例划分
    test_data = [] # 测试数据
    train_target = [] # 训练数据对应标签
    test_target = [] # 测试数据对应标签

    # 原始数据集分为 3 个类别，分别是 0~49,50~99,100~149，各50个
    for i in range(3):
        offset = 50 * i
        data = iris[offset+0:offset+50, :]
        # data = np.random.shuffle(data)
        np.random.shuffle(data) # 就地随机打乱

        # try:
        #     train_data.append(data[0:39, 1:5].tolist())
        #     train_target.append(data[0:39, 5].tolist())
        #     test_data.append(data[40:, 1:5].tolist())
        #     test_target.append(data[40:, 5].tolist())
        # except NameError:
        #     train_data = data[0:39, 1:5].tolist()
        #     train_target = data[0:39, 5].tolist()
        #     test_data = data[40:, 1:5].tolist()
        #     test_target = data[40:, 5].tolist()

        train_data.extend(data[0:40, 1:5].tolist())
        train_target.extend(data[0:40, 5].tolist())
        test_data.extend(data[40:, 1:5].tolist())
        test_target.extend(data[40:, 5].tolist())

    train_data = np.array(train_data)
    test_data = np.array(test_data)
    train_target = np.array(train_target)
    test_target = np.array(test_target)

    return train_data, test_data, train_target, test_target

# 计算距离
def calculateDistance(test_data, train_data) -> list:
    distance = []
    for i in range(len(test_data)):
        sub_dist = []
        for j in range(len(train_data)):
            dif_array = test_data[i] - train_data[j]
            dist = np.sqrt(np.sum(dif_array * dif_array))
            sub_dist.append(dist)
        
        distance.append(sub_dist)
    
    distance = np.array(distance)
    
    return distance

# 求解结果
def calculateResult(distance, K, train_target):
    results = []

    for i in range(len(distance)):
        index = np.argsort(distance[i])[:K]
        result = train_target[index]

        # result = pd.value_counts(result)

        species = Counter(result).most_common(1)[0][0]

        results.append(species)
    
    return results

# 评估结果
def estimateResult(results, test_target):
    right = 0
    print('-'*80)

    for i in range(len(results)):
        print('Right Species = ', test_target[i], \
            ', \tReal Species = ', results[i])

        if results[i] == test_target[i]:
            right += 1
        
    right_rate = right / len(results)
    print('-'*80)
    print("Right Rate: ", right_rate)
    print('-'*80)


    return

if __name__ == '__main__':
    print('-'*80)
    K = int(input("请输入 K 值："))

    train_data, test_data, train_target, test_target = getData()
    distance = calculateDistance(test_data, train_data)
    results = calculateResult(distance, K, train_target)

    estimateResult(results, test_target)




