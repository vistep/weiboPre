__author__ = 'Administrator'

# _*_ coding: utf-8 _*_

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# data = pd.read_table(r"weibo_train_data.txt", sep='\t', encoding='utf-8',
#                      header=None, names=['uid', 'mid', 'time', 'forward_count', 'comment_count', 'like_count', 'content'],
#                      dtype={'uid': str, 'mid': str, 'time': str, 'forward_count': int,
#                             'comment_count': int, 'like_count': int, 'content': str})
data = pd.read_table(r"weibo_train_data.txt", sep='\t', encoding='utf-8', header=None,
                     names=['uid', 'mid', 'time', 'forward_count', 'comment_count', 'like_count', 'content'])

print "max forwardCount: " + str(np.max(data['forward_count']))
print "mean forwardCount " + str(data['forward_count'].mean())
print "max commentCount: " + str(np.max(data['comment_count']))
print "mean commentCount " + str(data['comment_count'].mean())
print "max likeCount: " + str(np.max(data['like_count']))
print "mean likeCount " + str(data['like_count'].mean())

forwardArray = data['forward_count'].values
commentArray = data['comment_count'].values
likeArray = data['like_count'].values

print forwardArray[(forwardArray < 10) & (forwardArray > 0)].mean()
print forwardArray[(10 < forwardArray) & (forwardArray < 100)].mean()
print forwardArray[(100 < forwardArray) & (forwardArray < 1000)].mean()
print forwardArray[(1000 < forwardArray) & (forwardArray < 10000)].mean()
print forwardArray[forwardArray > 10000].mean()
# plt.figure(1)
# plt.hist(forwardArray, bins=range(0, 82000, 1000))
# plt.title("forwardCount")
# plt.figure(2)
# plt.hist(commentArray, bins=range(0, 36000, 1000))
# plt.title('commentCount')
# plt.figure(3)
# plt.hist(likeArray, bins=range(0, 8000, 1000))
# plt.title("likeCount")
# plt.show()
#
# print "forwardAndcomment"
# print data['forward_count'].corr(data['comment_count'])
# print "forwardAndlike"
# print data['forward_count'].corr(data['like_count'])
# print "commentAndLike"
# print data['comment_count'].corr(data['like_count'])


# ###############################################################################
# ################## calculate mean value ####################################

# userGroup = data.groupby(data.uid)
# user = userGroup.grouper.result_index.tolist()
# forwardMean = userGroup['forward_count'].mean().values.tolist()
# commentMean = userGroup['comment_count'].mean().values.tolist()
# likeMean = userGroup['like_count'].mean().values.tolist()
# table = dict(zip(user, zip(forwardMean, commentMean, likeMean)))
# totalforwardMean = data['forward_count'].mean()
# totalcommentMean = data['comment_count'].mean()
# totallikeMean = data['like_count'].mean()
# table['default'] = (totalforwardMean, totalcommentMean, totallikeMean)


# fr = open("weibo_predict_data.txt", 'r')
# fw = open("result.txt", 'w')
# try:
#     while True:
#         text = fr.readline()
#         if not text:
#             break
#         items = text.split("\t")
#         if table.get(items[0]):
#             forward, comment, like = table[items[0]]
#         else:
#             forward, comment, like = table['default']
#         toWrite = items[0] + '\t' + items[1] + '\t' + \
#                   str(int(forward)) + ',' + str(int(comment)) + ',' + str(int(like)) + '\n'
#         print toWrite
#         fw.write(toWrite)
# finally:
#     if fr:
#         fr.close()
#     if fw:
#         fw.close()

