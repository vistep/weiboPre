__author__ = 'Administrator'
# _*_ coding: utf-8 _*_
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.externals import joblib
from sklearn import ensemble

forward_x = np.loadtxt('./data/train_forward_0or1/x.txt', dtype=float, delimiter=u', ')
forward_y = np.loadtxt('./data/train_forward_0or1/y.txt', dtype=int)
comment_x = np.loadtxt('./data/train_comment_0or1/x.txt', dtype=float, delimiter=u', ')
comment_y = np.loadtxt('./data/train_comment_0or1/y.txt', dtype=int)
like_x = np.loadtxt('./data/train_like_0or1/x.txt', dtype=float, delimiter=u', ')
like_y = np.loadtxt('./data/train_like_0or1/y.txt', dtype=int)

forward_x_notZero = np.loadtxt('./data/train_forward_notZero/x.txt', dtype=float, delimiter=u', ')
forward_y_notZero = np.loadtxt('./data/train_forward_notZero/y.txt', dtype=int)
comment_x_notZero = np.loadtxt('./data/train_comment_notZero/x.txt', dtype=float, delimiter=u', ')
comment_y_notZero = np.loadtxt('./data/train_comment_notZero/y.txt', dtype=int)
like_x_notZero = np.loadtxt('./data/train_like_notZero/x.txt', dtype=float, delimiter=u', ')
like_y_notZero = np.loadtxt('./data/train_like_notZero/y.txt', dtype=int)

# forwardLR = sklearn.linear_model.LogisticRegression()
# commentLR = sklearn.linear_model.LogisticRegression()
# likeLR = sklearn.linear_model.LogisticRegression()
#
# forwardLR.fit(forward_x[0:1500000, :], forward_y[0:1500000])
# commentLR.fit(comment_x[0:1500000, :], comment_y[0:1500000])
# likeLR.fit(like_x[0:1500000, :], like_y[0:1500000])

# joblib.dump(forwardLR, './model/forwardLR.m')
# joblib.dump(commentLR, './model/commentLR.m')
# joblib.dump(likeLR, './model/likeLR.m')

# scoreF = forwardLR.score(forward_x[1500001:, :], forward_y[1500001:])
# scoreC = commentLR.score(comment_x[1500001:, :], comment_y[1500001:])
# scoreL = likeLR.score(like_x[1500001:, :], like_y[1500001:])

forwardRF = sklearn.ensemble.RandomForestClassifier()
commentRF = sklearn.ensemble.RandomForestClassifier()
likeRF = sklearn.ensemble.RandomForestClassifier()

forwardRF.fit(forward_x, forward_y)
commentRF.fit(comment_x, comment_y)
likeRF.fit(like_x, like_y)

joblib.dump(forwardRF, './model/forwardRF.m', compress=3)
joblib.dump(commentRF, './model/commentRF.m', compress=3)
joblib.dump(likeRF, './model/likeRF.m', compress=3)

forwardRF_notZero = sklearn.ensemble.RandomForestRegressor()
commentRF_notZero = sklearn.ensemble.RandomForestRegressor()
likeRF_notZero = sklearn.ensemble.RandomForestRegressor()

forwardRF_notZero.fit(forward_x_notZero, forward_y_notZero)
commentRF_notZero.fit(comment_x_notZero, comment_y_notZero)
likeRF_notZero.fit(like_x_notZero, like_y_notZero)

joblib.dump(forwardRF_notZero, './model/forwardRF_notZero.m', compress=3)
joblib.dump(commentRF_notZero, './model/commentRF_notZero.m', compress=3)
joblib.dump(likeRF_notZero, './model/likeRF_notZero.m', compress=3)

# forwardRF.fit(forward_x[0:1500000, :], forward_y[0:1500000])
# commentRF.fit(comment_x[0:1500000, :], comment_y[0:1500000])
# likeRF.fit(like_x[0:1500000, :], like_y[0:1500000])

# scoreF = forwardRF.score(forward_x[1500001:, :], forward_y[1500001:])
# scoreC = commentRF.score(comment_x[1500001:, :], comment_y[1500001:])
# scoreL = likeRF.score(like_x[1500001:, :], like_y[1500001:])
#
# print type(scoreF)
# print "forward score"
# print scoreF
# print "comment score"
# print scoreC
# print "comment score"
# print scoreL
