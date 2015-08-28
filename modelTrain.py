__author__ = 'Administrator'
# _*_ coding: utf-8 _*_
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.externals import joblib

forward_x = np.loadtxt('./data/train_forward_0or1/x.txt', dtype=float, delimiter=u', ')
forward_y = np.loadtxt('./data/train_forward_0or1/y.txt', dtype=int)
comment_x = np.loadtxt('./data/train_comment_0or1/x.txt', dtype=float, delimiter=u', ')
comment_y = np.loadtxt('./data/train_comment_0or1/y.txt', dtype=int)
like_x = np.loadtxt('./data/train_like_0or1/x.txt', dtype=float, delimiter=u', ')
like_y = np.loadtxt('./data/train_like_0or1/y.txt', dtype=int)

forwardLR = sklearn.linear_model.LogisticRegression()
commentLR = sklearn.linear_model.LogisticRegression()
likeLR = sklearn.linear_model.LogisticRegression()

forwardLR.fit(forward_x, forward_y)
commentLR.fit(comment_x, comment_y)
likeLR.fit(like_x, like_y)

joblib.dump(forwardLR, './model/forwardLR.m')
joblib.dump(commentLR, './model/commentLR.m')
joblib.dump(likeLR, './model/likeLR.m')
