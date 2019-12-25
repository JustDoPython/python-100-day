#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Daijingbo
# @Date  : 2019/6/16
# @Desc  :FBP ML XGBClassifier
# http://www.captainbed.net/blog-acredjb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xgboost as xgb
from xgboost import plot_importance
from xgboost import XGBClassifier
# from sklearn import preprocessing
# from sklearn.preprocessing import Imputer
from sklearn.feature_extraction import DictVectorizer
# from sklearn.cross_validation import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
#20190706 https://segmentfault.com/a/1190000019109124?utm_medium=referral&utm_source=tuicool
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer
from sklearn.metrics import f1_score
from time import time
from sklearn.metrics import accuracy_score
def predict_labels(model, features, target):
    ''' 使用模型进行预测 '''
    # 记录预测时长
    start = time()
    y_pred = model.predict(features)
    end = time()
    print("预测时间 in {:.4f} 秒".format(end - start))
    return f1_score(target, y_pred, pos_label=1), sum(target == y_pred) / float(len(y_pred))
def trainandTest(X, y,X_t):
    # X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.25, random_state=33)#0.33  7
    X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.33, random_state=0)  # 0.33  7
    ### feature_extraction
    #####特征向量化############
    vec=DictVectorizer(sparse=False)
    ###########归一化和标准化#################
    X_train=vec.fit_transform(X_train.to_dict(orient='record'))
    X_test=vec.transform(X_t.to_dict(orient='record'))
    #20190706
    # 设置想要自动调参的参数
    # parameters={'n_estimators': [90, 100, 110],
    #             'max_depth': [5, 6, 7],
    #             }
    # model=XGBClassifier(seed=42)  #
    # f1_scorer=make_scorer(f1_score, pos_label=1)
    # # 使用 grdi search 自动调参
    # grid_obj=GridSearchCV(model,
    #                       scoring=f1_scorer,
    #                       param_grid=parameters,
    #                       cv=5)
    # grid_obj=grid_obj.fit(X_train, y_train)
    # # 得到最佳的模型
    # model=grid_obj.best_estimator_
    # # print(model)
    # # 查看最终的模型效果
    # f1, acc=predict_labels(model, X_train, y_train)
    # print("F1 score and accuracy score for training set: {:.4f} , {:.4f}。".format(f1, acc))
    #
    # f1, acc=predict_labels(model, X_test, y_test)
    # print("F1 score and accuracy score for test set: {:.4f} , {:.4f}。".format(f1, acc))
############第三处调参：选择全参数和无参数（默认）################################
    # model=xgb.XGBClassifier(learning_rate =0.1,n_estimators=1000,max_depth=4,min_child_weight=6,gamma=0,subsample=0.8,colsample_bytree=0.8,reg_alpha=0.005,objective='binary:logistic',nthread=4,scale_pos_weight=1,seed=27)
    model=XGBClassifier()#ok无参数
    model.fit(X_train,y_train)
    # 对测试集进行预测
    ans = model.predict(X_test)
    # print(model)
    ans_len = len(ans)
    # print("ans_len:"+str(ans_len))#打印这行再屏蔽就不报错：index  is out of bounds for axis 0 with size
    id_list = np.arange(5953, 5975)
    data_arr = []
    for row in range(0, ans_len):
        data_arr.append([int(id_list[row]), ans[row]])
        # data_arr.append([id_list, ans[row]])
        print(ans[row])
    np_data = np.array(data_arr)
    # 写入文件
    pd_data = pd.DataFrame(np_data, columns=['id', 'y'])
    pd_data.to_csv('FBP_submit.csv', index=None)
    # # 显示重要特征
    # plot_importance(model)
    # plt.show()
    #evaluate prediction
    # predictions = [round(value) for value in ans]
    # accuracy = accuracy_score(y_test,predictions)
    # print("Accurary:%2.f%%"%(accuracy * 100.0))
if __name__ == '__main__':
    f0='ysb';  # bet365
    f1='li';  # 8jbb
    f2='bet365';  # wl
    f3='SNAI';  # 10ysb  ,hg
    f4='wl';
    f5='ms';
    f6='ao';  # li
    f7='w';
    f8='10bet';
    f9='hg';  # interw
    f10='interw';  # 9ms
################第一处调参：选择训练集数据的行数1000-4000-all##################
    # trainFilePath='E:/PythonLearn/pc_ex/AdaBoost_PeiLv/FBP_train-1000.csv'
    trainFilePath = 'E:/PythonLearn/pc_ex/AdaBoost_PeiLv/FBP_train.csv'
    # trainFilePath='E:/PythonLearn/pc_ex/AdaBoost_PeiLv/FBP_train-3000.csv'
    # trainFilePath = 'E:/PythonLearn/pc_ex/AdaBoost_PeiLv/FBP_train-all.csv'
    testFilePath = 'E:/PythonLearn/pc_ex/AdaBoost_PeiLv/FBP_predict.csv'
    data = pd.read_csv(trainFilePath)
    X_test= pd.read_csv(testFilePath)
###############第二处调参：选择全部特征还是部分特征###########################
    X_train=data[[f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]]#全特征
    # X_train=data[[f10, f7, f5,f6]]
    y_train=data['y']
    trainandTest(X_train, y_train,X_test)
