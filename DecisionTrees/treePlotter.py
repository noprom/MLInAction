# coding=utf-8
'''
@title: treePlotter

@author: tyee.noprom@qq.com
Created on 2/22/16
'''
import matplotlib.pyplot as plt

decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leftNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")

def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy = parentPt, xycoords = 'axes fraction',
                            xytext = centerPt, textcoords = 'axes fraction',
                            va = "center", ha = "center", bbox = nodeType, arrowprops = arrow_args)

def createPlot(inTree):
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    # axprops = dict(xticks=[], yticks=[])
    # createPlot.ax1 = plt.subplot(111, frameon=False, **axprops) #no ticks
    createPlot.ax1 = plt.subplot(111, frameon=False) #ticks for demo puropses
    plotNode('a decision tree', (0.5, 0.1), (0.1, 0.5), decisionNode)
    plotNode('a left node', (0.8, 0.1), (0.3, 0.8), leftNode)
    plt.show()

# show the tree
import trees
myDat,labels=trees.createDataSet()
createPlot(myDat)