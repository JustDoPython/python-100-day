from math import  log
import operator


def createDataSet():
    '''
    创建数据集
    '''

    dataSet = [[1, 1, 0, 'y'],
               [1, 1, 0, 'y'],
               [1, 0, 0, 'n'],
               [0, 1, 0, 'n'],
               [0, 0, 1, 'n'],
               [1, 0, 1, 'n'],
               [1, 1, 1, 'n']]
    labels = ['Salary', 'Time', 'Bank flow']
    return dataSet,labels


def calcEntropy(dataSet):
    '''
    计算熵
    :param dataSet: 数据集
    :return: 熵值
    '''

    numEntries = len(dataSet)
    labelCounts = {}
    for line in dataSet:
        currentLabel = line[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    entropy = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        entropy -= prob * log(prob, 2)
    return entropy


def splitDataSet(dataSet,axis,value):
    '''
    划分数据集
    :param dataSet: 按照给定特征划分数据集
    :param axis: 划分数据集的特征
    :param value: 需要返回的特征的值
    :return: 经验熵
    '''
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis]==value:
            reducedFeatVec=featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet




def chooseBestFeatureToSplit(dataSet):
    '''
    计算数据集的熵
    :param dataSet: 数据集
    :return: 最优的特征值的索引
    '''

    # 特征个数
    numFeatures = len(dataSet[0]) - 1
    # 数据集的熵
    baseEntropy = calcEntropy(dataSet)
    # 最优信息增益
    bestInfoGain = 0.0
    # 最优特征的索引值
    bestFeature = -1

    for i in range(numFeatures):
        # 获取数据集的第 i 个所有特征
        featList = [example[i] for example in dataSet]
        #创建 set集合{}，元素不可重复
        uniqueVals = set(featList)
        # 经验条件熵
        newEntropy = 0.0
        #计算信息增益
        for value in uniqueVals:
            # 数据集划分后的子集
            subDataSet = splitDataSet(dataSet, i, value)
            #计算子集的概率
            prob = len(subDataSet) / float(len(dataSet))
            #根据公式计算经验条件熵
            newEntropy += prob * calcEntropy((subDataSet))
        #信息增益
        infoGain = baseEntropy - newEntropy
        #打印每个特征的信息增益
        print("第%d个特征属性的信息增益为%.3f" % (i, infoGain))

        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


def majorityCnt(classList):
    '''
    类别数多的类别
    :param classList: 类别
    :return: 返回类别数多的类别
    '''
    classCount={}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def createTree(dataSet,labels):
    '''
    构建决策树
    :param dataSet: 数据集样本
    :param labels: 特征属性
    :return: 决策树
    '''

    # 决策类别
    classList = [example[-1] for example in dataSet]
    # 类别完全相同停止继续划分
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    # 返回出现次数最多的类别
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    # 返回最优的特征属性
    bestFeature = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeature]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeature])
    # 最优特征值
    featureValues = [example[bestFeature] for example in dataSet]
    uniqueVals = set(featureValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeature, value), subLabels)
    return myTree



mydata,labels = createDataSet()

# entropy = splitDataSet(mydata,0,1 )

# print("最优的索引值为：", str(chooseBestFeatureToSplit(mydata)))

print(createTree(mydata, labels))
