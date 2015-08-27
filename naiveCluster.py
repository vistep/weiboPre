__author__ = 'Administrator'
# _*_ coding: utf-8 _*_
__metaclass__ = type
import numpy as np


class Center:
    def __init__(self, data, index):
        self.sampleArr = np.array(data)
        self.indexLst = []
        self.indexLst.append(index)
        self.meanValue = data

    def add(self, data, index):
        self.sampleArr = np.vstack((self.sampleArr, data))
        self.indexLst.append(index)
        self.meanValue = self.sampleArr.mean(axis=0)

    def getNum(self):
        return len(self.indexLst)

def loadData():
    # every row contains one sample
    return np.array([[1, 2, 3], [1, 2, 4], [7, 8, 9]])

def distance(data1, data2):
    # need to be redefined
    return np.sum((data1 - data2) ** 2) / np.shape(data1)[0]

def process():
    limit = 0.5 ### need to be modified
    dataSet = loadData()
    print "dataSet"
    print dataSet
    centerLst = []
    centerLst.append(Center(dataSet[0, :], 0))
    for lines in range(1, np.shape(dataSet)[1]):
        dis = np.zeros((1, len(centerLst)))
        for i in range(0, len(centerLst)):
            print centerLst
            dis[0, i] = distance(centerLst[i].meanValue, dataSet[lines, :])
        minDis = dis.min()
        if minDis < limit:
            index = np.argmin(dis)
            centerLst[index].add(dataSet[lines, :], lines)
        else:
            centerLst.append(Center(dataSet[lines, :], lines))
    return centerLst

if __name__ == '__main__':
    result = process()
    print "result"
    for item in result:
        print item.getNum()

