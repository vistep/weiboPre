# -*- coding: utf-8 -*-

import csv

#if __name__=='__main__':
import codecs
fr = codecs.open(r'weibo_train_data.txt', mode='r', encoding='utf-8')
lines = fr.readlines()
fr.close()
try:
    fw = open(r"weibo_train.csv", 'wb')
    for line in lines:
        line = line.strip().split('\t')
        for i in range(len(line)-1):
            fw.write(line[i]+',')
        fw.write(line[-1].encode('utf-8')+'\n')
except:
    print line[-1]
    raise
finally:
    fw.close()
