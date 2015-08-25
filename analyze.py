__author__ = 'Administrator'

# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_table(r"weibo_train_data.txt", sep='\t', encoding='utf-8',
                     header=None, names=['uid', 'mid', 'time', 'forward_count', 'comment_count', 'like_count', 'content'],
                     dtype={'uid': str, 'mid': str, 'time': str, 'forward_count': int,
                            'comment_count': int, 'like_count': int, 'content': str})

# print "max forwardCount: " + str(np.max(data['forward_count']))
# print "mean forwardCount " + str(data['forward_count'].mean())
# print "max commentCount: " + str(np.max(data['comment_count']))
# print "mean commentCount " + str(data['comment_count'].mean())
# print "max likeCount: " + str(np.max(data['like_count']))
# print "mean likeCount " + str(data['like_count'].mean())
#
# forwardArray = data['forward_count'].values
# commentArray = data['comment_count'].values
# likeArray = data['like_count'].values
#
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

userGroup = data.groupby(data.uid)

