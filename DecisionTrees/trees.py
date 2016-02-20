# coding=utf-8
'''
@title: 决策树

@author: tyee.noprom@qq.com
Created on 2/20/16
'''

from math import log

def calcShanonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for fectVec in dataSet:
        currentLabel = fectVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
            labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt