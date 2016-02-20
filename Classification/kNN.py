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

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet)) #创建一个零矩阵,大小和原来的矩阵一样
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1)) #element wise divide
    return normDataSet, ranges, minVals

def datingClassTest():
    hoRatio = 0.50 #hold out 10%
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt') #load the data
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0] #读取矩阵第一维的长度
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs: m], 3)
        print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i])
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print "the total error rate is: %f" % (errorCount / float(numTestVecs))
    print errorCount

def classifyPerson():
    resultList = ['not at all', 'in small doses', 'in large doses']
    percentTats = float(raw_input("percentage of time spent playing video games?"))
    ffMiles = float(raw_input("frequent flier miles earned per year?"))
    iceCream = float(raw_input("liters of ice cream consumes per year?"))
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles, percentTats, iceCream])
    classifierResult = classify0((inArr - minVals)/ranges, normMat, datingLabels, 3)
    print "You will probably like this person:", resultList[classifierResult - 1]