'''
__author__ = justdopython.com
'''
import numpy as np
import pandas as pd
import random


class Clusters():
    def __init__(self, train_data, K):
        '''
        :params train_data: ndarray. 训练数据.
        :params K: int. 要划分的簇的数量.

        :attr train_data:
        '''
        super().__init__()

        self.train_data = train_data
        self.K = K
        # 标记聚类是否完成。具体的真假，取决于是否还存在需要从一个簇移动到另一个簇的数据
        self.finished = False

        # 随机选取 K 个数据作为各个簇的中心点
        index = random.sample(range(len(self.train_data)), self.K)
        self.centroid = train_data[index, 1:5]

        # 将训练数据均匀分配到各个簇，以便以同一的形式适用于数据的分配
        self.clusters = []
        offset = len(train_data) // self.K
        for i in range(self.K):
            start = offset * i
            if i < self.K-1:
                self.clusters.append(train_data[start:start+offset,:])
            else:
                # 最后一个簇包含剩下的所有数据
                self.clusters.append(train_data[start:,:])
                

    # 加载所要用到的数据集
    @staticmethod
    def getData():
        '''
        获取数据，返回值类型为 ndarray
        '''
        train_data = pd.read_csv('iris.csv').to_numpy()

        return train_data

    # 将各数据分配到每个簇中去
    def assign(self):
        self.finished = True
        # data_index_list 和 target_index_list 分别记录“需要移动的数据在当前簇中的索引”以及“要移动到的目标簇索引”
        target_index_list = []
        data_index_list = []
        for i in range(self.K):
            target_index_list.append([])
            data_index_list.append([])

        for cluster_index in range(len(self.clusters)):
            for data_index in range(len(self.clusters[cluster_index])):
                diff = self.clusters[cluster_index][data_index, 1:5] - self.centroid
                distance_square = np.sum(diff * diff, axis=1)
                target_index = np.argmin(distance_square)

                if cluster_index != target_index:
                    self.finished = False
                    target_index_list[cluster_index].append(target_index)
                    data_index_list[cluster_index].append(data_index)
        
        for cluster_index in range(self.K):
            for index in range(len(target_index_list[cluster_index])):
                target_index = target_index_list[cluster_index][index]
                data_index = data_index_list[cluster_index][index]

                self.clusters[target_index] = np.append(self.clusters[target_index], 
                                                        self.clusters[cluster_index][data_index, :]).reshape(-1, 6)

        for cluster_index in range(self.K):
            data_index = data_index_list[cluster_index]
            self.clusters[cluster_index] = np.delete(self.clusters[cluster_index], data_index, axis=0)


    # 更新各个簇的质心
    def update(self):
        for cluster_index in range(len(self.clusters)):
            self.centroid[cluster_index] = np.mean(self.clusters[cluster_index][:,1:5], axis=0)

    def train(self):
        '''
        进行聚类训练
        '''
        while not self.finished:
            self.assign()
            self.update()
        print('训练完成！！！')

    def printResult(self):
        '''
        打印聚类结果
        '''
        print('-'*80)
        print('*'*80)
        print('-'*80)
        print('*'*30, '聚类结果', '*'*30)
        print('-'*30,'各簇中心','-'*30)
        for i in range(self.K):
            print('第', str(i), '簇中心：', self.centroid[i])
        print('-'*80)
        print('-'*30,'各簇结果','-'*30)
        for i in range(self.K):
            print('-'*20, '第', str(i), '簇结果', '-'*20,)
            for d in self.clusters[i]:
                print(d[5])

        print('-'*80)
        print('*'*80)
        print('-'*80)




if __name__ == '__main__':
    print('-'*80)
    K = int(input('请输入要划分的簇数（应为正整数）：'))
    data = Clusters.getData()
    clusters = Clusters(data, K)

    clusters.train()

    clusters.printResult()