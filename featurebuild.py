# _*_ coding: utf-8 _*_
import codecs
import pandas as pd
import numpy as np

# #####calculate user mean
train_data = pd.read_table(r"weibo_train_data.txt", sep='\t', encoding='utf-8', header=None,
                           names=['uid', 'mid', 'time', 'forward_count', 'comment_count', 'like_count', 'content'])
userGroup = train_data.groupby(train_data.uid)
user = userGroup.grouper.result_index.tolist()
forwardMean = userGroup['forward_count'].mean().values.tolist()
commentMean = userGroup['comment_count'].mean().values.tolist()
likeMean = userGroup['like_count'].mean().values.tolist()
train_table = dict(zip(user, zip(forwardMean, commentMean, likeMean)))
totalforwardMean = train_data['forward_count'].mean()
totalcommentMean = train_data['comment_count'].mean()
totallikeMean = train_data['like_count'].mean()
train_table['default'] = (totalforwardMean, totalcommentMean, totallikeMean)

# ####build feature
fr1 = codecs.open('weibo_train_data.txt', mode='r', encoding='utf-8')
fr2 = codecs.open('weibo_predict_data.txt', mode='r', encoding='utf-8')
fw1 = codecs.open('train_feature.txt', mode='w', encoding='utf-8')
fw2 = codecs.open('predict_feature.txt', mode='w', encoding='utf-8')
# ###train feature
try:
    while True:
        text = fr1.readline()
        if not text:
            break
        items = text.split('\t')
        if items[0] == u'\r\n':
            continue
        feature = [None] * 8
        feature[0], feature[1], feature[2] = train_table[items[0]] if items[0] in train_table else train_table['default']
        feature[3] = 0
        feature[4] = 1 if u'@' in items[-1] else 0
        feature[5] = 1 if u'#' in items[-1] else 0
        feature[6] = 1 if u'http:' in items[-1] else 0
        feature[7] = 1 if u'转发' in items[-1] else 0
        try:
            toWrite = items[0] + '\t' + items[1] + '\t' + str(feature) + '\n'
            fw1.write(toWrite)
        except IndexError:
            continue
    while True:
        text = fr2.readline()
        if not text:
            break
        items = text.split('\t')
        if items[0] == u'\r\n':
            continue
        feature = [None] * 8
        feature[0], feature[1], feature[2] = train_table[items[0]] if items[0] in train_table else train_table['default']
        feature[3] = 0
        feature[4] = 1 if u'@' in items[-1] else 0
        feature[5] = 1 if u'#' in items[-1] else 0
        feature[6] = 1 if u'http:' in items[-1] else 0
        feature[7] = 1 if u'转发' in items[-1] else 0
        try:
            toWrite = items[0] + '\t' + items[1] + '\t' + str(feature) + '\n'
            fw2.write(toWrite)
        except IndexError:
            continue
finally:
    if not fw1:
        fw1.close()
    if not fw2:
        fw2.close()



