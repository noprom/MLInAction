'''
@title:kNN算法

@author: tyee.noprom@qq.com
Created on 2/19/16
'''
from numpy import *
import operator
from os import listdir

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels