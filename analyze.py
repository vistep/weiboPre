__author__ = 'Administrator'

# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_table(r"weibo_train_data.txt", sep='\t', encoding='utf-8',
                     dtype={'uid': str, 'mid': str, 'time': str, 'forward_count': int,
                            'comment_count': int, 'like_count': int, 'content': str})

print "max forwardCount: " + str(np.max(data['forward_count']))
print "mean forwardCount " + str(data['forward_count'].mean())
print "max commentCount: " + str(np.max(data['comment_count']))
print "mean commentCount " + str(data['comment_count'].mean())
print "max likeCount: " + str(np.max(data['like_count']))
print "mean likeCount " + str(data['like_count'].mean())
plt.figure(1)
plt.hist(data['forward_count'])
subdata = data[data.forward_count > 1000]
print subdata['forward_count'].head()
print len(subdata['forward_count'])
plt.figure(2)
plt.hist(subdata['forward_count'])
plt.show()
