#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Daijingbo
# @Date  : 2019/5/27
# @Desc  :FBP ML
# http://www.captainbed.net/blog-acredjb
import pandas as pd
import matplotlib.pyplot as plt
import xgboost as xgb
from sklearn import preprocessing
import numpy as np
from xgboost import plot_importance
from sklearn.preprocessing import Imputer
# from sklearn.cross_validation import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split

def featureSet(data):
    imputer = Imputer(missing_values='NaN', strategy='mean', axis=1)
    imputer.fit(data.loc[:, ['10bet', 'jbb', 'ms', 'ysb', 'Pinnacle', 'SNAI']])
    x_new = imputer.transform(data.loc[:, ['10bet', 'jbb', 'ms', 'ysb', 'Pinnacle', 'SNAI']])

    data_num = len(data)
    XList = []
    for row in range(0, data_num):
        tmp_list = []
        tmp_list.append(data.iloc[row]['Oddset'])
        tmp_list.append(data.iloc[row]['li'])
        tmp_list.append(data.iloc[row]['bet365'])
        tmp_list.append(data.iloc[row]['interw'])
        tmp_list.append(data.iloc[row]['wl'])
        tmp_list.append(data.iloc[row]['w'])
        tmp_list.append(data.iloc[row]['ao'])
        # tmp_list.append(data.iloc[row]['10bet'])
        # tmp_list.append(data.iloc[row]['jbb'])
        # tmp_list.append(data.iloc[row]['ms'])
        # tmp_list.append(data.iloc[row]['ysb'])
        tmp_list.append(x_new[row][0])
        tmp_list.append(x_new[row][1])
        tmp_list.append(x_new[row][2])
        tmp_list.append(x_new[row][3])
        tmp_list.append(x_new[row][4])
        tmp_list.append(x_new[row][5])
        XList.append(tmp_list)
    yList = data.y.values
    return XList, yList

def loadTestData(filePath):
    data = pd.read_csv(filepath_or_buffer=filePath)
    imputer = Imputer(missing_values='NaN', strategy='mean', axis=1)
    imputer.fit(data.loc[:, ['10bet', 'jbb', 'ms', 'ysb', 'Pinnacle', 'SNAI']])
    x_new = imputer.transform(data.loc[:, ['10bet', 'jbb', 'ms', 'ysb', 'Pinnacle', 'SNAI']])

    data_num = len(data)
    XList = []
    for row in range(0, data_num):
        tmp_list = []
        tmp_list.append(data.iloc[row]['Oddset'])
        tmp_list.append(data.iloc[row]['li'])
        tmp_list.append(data.iloc[row]['bet365'])
        tmp_list.append(data.iloc[row]['interw'])
        tmp_list.append(data.iloc[row]['wl'])
        tmp_list.append(data.iloc[row]['w'])
        tmp_list.append(data.iloc[row]['ao'])
        # tmp_list.append(data.iloc[row]['10bet'])
        # tmp_list.append(data.iloc[row]['jbb'])
        # tmp_list.append(data.iloc[row]['ms'])
        # tmp_list.append(data.iloc[row]['ysb'])
        tmp_list.append(x_new[row][0])
        tmp_list.append(x_new[row][1])
        tmp_list.append(x_new[row][2])
        tmp_list.append(x_new[row][3])
        tmp_list.append(x_new[row][4])
        tmp_list.append(x_new[row][5])
        XList.append(tmp_list)
    return XList

def trainandTest(X_train, y_train, X_test):
    # XGBoost训练过程
    model = xgb.XGBRegressor(max_depth=2, learning_rate=0.01, n_estimators=500, silent=False, objective='reg:gamma')
    model.fit(X_train, y_train)

    # 对测试集进行预测
    ans = model.predict(X_test)
    ans_len = len(ans)
    id_list=np.arange(5953, 5975)
    data_arr = []
    for row in range(0, ans_len):
        data_arr.append([int(id_list[row]), ans[row]])
        # data_arr.append([id_list, ans[row]])
        print(ans[row])
    np_data = np.array(data_arr)

    # 写入文件
    pd_data = pd.DataFrame(np_data, columns=['id', 'y'])
    pd_data.to_csv('FBP_submit.csv', index=None)

    # 显示重要特征
    plot_importance(model)
    plt.show()

if __name__ == '__main__':
    trainFilePath = 'E:/PythonLearn/pc_ex/AdaBoost_PeiLv/FBP_train.csv'
    testFilePath = 'E:/PythonLearn/pc_ex/AdaBoost_PeiLv/FBP_predict.csv'
    data = pd.read_csv(trainFilePath)
    X_train, y_train = featureSet(data)
    X_test = loadTestData(testFilePath)
    trainandTest(X_train, y_train, X_test)
