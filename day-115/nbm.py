
import pandas as pd
import numpy as np

class Nbm(object):

    def getSampleSet(self):
        dataSet = np.array(pd.read_csv('csv文件地址'))  #将数据转为数组
        featureData = dataSet[:, 0 : dataSet.shape[1] - 1] #取出特征
        labels = dataSet[:, dataSet.shape[1] - 1] #取出类别
        return featureData, labels


    def priori(self, labels):
        # 求出是和否的先验概率
        labels = list(labels)
        priori_ny = {}
        for label in labels:
            priori_ny[label] = labels.count(label) / float(len(labels)) # P = count(label) / count(labels)
        return priori_ny

    def feature_probability(self, priori_ny, features):
        # 求出特征概率：多云+是，多云+否，冷+是，冷+否同时发生的概率
        p_feature_ny = {}
        for ny in priori_ny.keys():
            ny_index = [i for i, label in enumerate(labels) if label == ny] # 是、否的下标
            for j in range(len(features)):
                f_index = [i for i, feature in enumerate(trainData[:, j]) if feature == features[j]] # 特征的下标
                xy_count = len(set(f_index) & set(ny_index)) # 类别和特征下标相同的长度
                pkey = str(features[j]) + '+' + str(ny)
                p_feature_ny[pkey] = xy_count / float(len(labels)) # 特征和类别同时发生的概率
        return p_feature_ny

    def conditional_probability(self, priori_ny, feature_probability, features):
        #求出条件概率
        P = {}
        for y in priori_ny.keys():
            for x in features:
                pkey = str(x) + '|' + str(y)
                P[pkey] = feature_probability[str(x) + '+' + str(y)] / float(priori_ny[y])  # P[X1/Y] = P[X1Y]/P[Y]
        return P

    def classify(self, priori_ny, feature_probability, features):


        #求条件概率
        p = self.conditional_probability(priori_ny, feature_probability, features)

        #求出[多云、冷、低、弱]所属类别
        f = {}
        for ny in priori_ny:
            f[ny] = priori_ny[ny]
            for x in features:
                f[ny] = f[ny] * p[str(x)+'|'+str(ny)]   #计算P(多云∣是)∗P(冷∣是)∗P(低∣是)∗P(弱∣是)∗P(是)

        return max(f, key=f.get)  #概率最大值对应的类别


if __name__ == '__main__':
    nbm = Nbm()
    features = ['多云', '冷', '低', '弱']
    trainData, labels = nbm.getSampleSet()
    priori_ny = nbm.priori(labels)

    feature_probability = nbm.feature_probability(priori_ny, features)



    result = nbm.classify(priori_ny, feature_probability, features)

    print(features, '的结果是', result)
