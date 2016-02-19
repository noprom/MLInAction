# coding=utf-8
'''
@title:kNN算法
@author: tyee.noprom@qq.com
Created on 2/19/16
'''
from numpy import *
import operator
from os import listdir

def classify0(inX, dataSet, labels, k):
    'kNN分类'
    # shape是一个矩阵里面的元素
    dataSetSize = dataSet.shape[0]
    # tile函数用于重复某个数组
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    # 平方
    sqDiffMat = diffMat ** 2
    # axis=1以后就是将一个矩阵的每一行向量相加
    sqDistances = sqDiffMat.sum(axis = 1)
    # 开根号求距离
    distances = sqDistances ** 0.5
    # argsort函数返回的是数组值从小到大的索引值
    sortedDistIndicies = distances.argsort()
    # 元组
    classCount = {}
    for i in range(k):
        # 统计k个类出现的次数
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    # 排序产生一个新的列表返回
    # operator.itemgetter(1):根据出现的次数进行排序
    # reversed: 默认False,从小大大;若为True则从大到小
    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse = True)
    # 返回出现次数最多的类名字
    return sortedClassCount[0][0]

def createDataSet():
    '创建一个数据集合'
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def file2matrix(filename):
    '将文件内容转化为矩阵'
    fr = open(filename)
    numberOfLines = len(fr.readlines())         #get the number of lines in the file
    returnMat = zeros((numberOfLines,3))        #prepare matrix to return
    classLabelVector = []                       #prepare labels return
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        #classLabelVector.append(int(listFromLine[-1]))
        classLabelVector.append(listFromLine[-1])
        index += 1
    return returnMat,classLabelVector