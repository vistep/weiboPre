__author__ = 'Administrator'
# _*_ coding: utf-8 _*_
__metaclass__ = type
import numpy as np
import codecs

class Center:
    def __init__(self, data, index):
        self.sumArr = np.array(data)
        self.indexLst = []
        self.indexLst.append(index)
        self.meanValue = data
        self.num = 1

    def add(self, data, index):
        self.sumArr += data
        self.indexLst.append(index)
        self.num += 1
        self.meanValue = self.sumArr / self.num

    def merge(self, center2):
        self.sumArr += center2.sumArr
        self.indexLst += center2.indexLst
        self.num += center2.num
        self.meanValue = self.sumArr / self.num


def loadData():
    # every row contains one sample
    return np.array([[1, 2, 3], [1, 2, 4], [7, 8, 9]])


def distance(data1, data2):
    # need to be redefined
    return np.sum((data1 - data2) ** 2) / (np.size(np.nonzero(data1)) + np.size(np.nonzero(data2)))

# def process():
#     limit = 0.2 ### need to be modified
#     dataSet = loadData()
#     print "dataSet"
#     print dataSet
#     centerLst = []
#     centerLst.append(Center(dataSet[0, :], 0))
#     for lines in range(1, np.shape(dataSet)[1]):
#         dis = np.zeros((1, len(centerLst)))
#         for i in range(0, len(centerLst)):
#             print centerLst
#             dis[0, i] = distance(centerLst[i].meanValue, dataSet[lines, :])
#         minDis = dis.min()
#         if minDis < limit:
#             index = np.argmin(dis)
#             centerLst[index].add(dataSet[lines, :], lines)
#         else:
#             centerLst.append(Center(dataSet[lines, :], lines))
#     return centerLst

def process(filename):
    limit = 0.28  # ## need to be modified
    fr = codecs.open(filename, mode='r', encoding='utf-8')
    centerLst = []
    text = fr.readline()
    items = text.split('\t')
    xdata = np.fromstring(items[1][0:-1], dtype=float, sep=', ')
    centerLst.append(Center(xdata, items[0]))
    while True:
        text = fr.readline()
        if not text:
            break
        items = text.split('\t')
        if len(items[1]) < 2:
            continue
        xdata = np.fromstring(items[1][0:-1], dtype=float, sep=', ')
        print items[0]
        dis = np.zeros((len(centerLst)))
        for i in range(0, len(centerLst)):
            dis[i] = distance(centerLst[i].meanValue, xdata)
        mindis = dis.min()
        # print mindis
        if mindis < limit:
            index = np.argmin(dis)
            centerLst[index].add(xdata, items[0])
        else:
            centerLst.append(Center(xdata, items[0]))
    fr.close()
    return centerLst

def mergelist(centerlist1, centerlist2):
    threshold = 0.14
    for center2 in centerlist2:
        dis = np.zeros((len(centerlist1)))
        for i in range(0, len(centerlist1)):
            dis[i] = distance(centerlist1[i].meanValue, center2.meanValue)
        mindis = dis.min()
        if mindis < threshold:
            index = np.argmin(dis)
            centerlist1[index].merge(center2)
        else:
            centerlist1.append(center2)
    return centerlist1

if __name__ == '__main__':
    # filename = './data/wordVectorSample1.txt'
    # resultLst = process(filename)
    filename = ['./data/wordVectorSample1.txt', './data/wordVectorSample2.txt', './data/wordVectorSample3.txt',
                './data/wordVectorSample4.txt', './data/wordVectorSample5.txt', './data/wordVectorSample6.txt',
                './data/wordVectorSample7.txt', './data/wordVectorSample8.txt']
    resultLst = map(process, filename)
    print "merging..."
    resultLst = reduce(mergelist, resultLst)
    print "count..."
    table = {}
    for center in resultLst:
        for index in center.indexLst:
            table[index] = center.num
    fw = codecs.open('./data/junkScore.txt', mode='w', encoding='utf-8')
    for i in range(0, 1626750):
        if str(i) in table:
            fw.write(str(i) + '\t' + str(table[str(i)]) + '\n')
        else:
            fw.write(str(i) + '\t' + str(1) + '\n')
    print "done"


