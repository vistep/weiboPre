__author__ = 'Administrator'
# _*_ coding: utf-8 _*_
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.externals import joblib
from sklearn import ensemble
import codecs

forward_classifier = joblib.load('./model/forwardRF.m')
forward_Regressor = joblib.load('./model/forwardRF_notZero.m')
comment_classifier = joblib.load('./model/commentRF.m')
comment_Regressor = joblib.load('./model/commentRF_notZero.m')
like_calssifier = joblib.load('./model/likeRF.m')
like_Regressor = joblib.load('./model/likeRF_notZero.m')

fr = codecs.open('./data/predict_feature.txt', mode='r', encoding='utf-8')
fw = codecs.open('result.txt', mode='w', encoding='utf-8')
try:
    while True:
        text = fr.readline()
        if not text:
            break
        items = text.split('\t')
        xString = items[-1][1:-2]
        x = np.fromstring(xString, dtype=float, sep=u', ')
        forward = forward_classifier.predict(x)
        if forward == 0:
            forward = 0
        else:
            forward = forward_Regressor.predict(x).tolist()[0]
        comment = comment_classifier.predict(x)
        if comment == 0:
            comment = 0
        else:
            comment = comment_Regressor.predict(x).tolist()[0]
        like = like_calssifier.predict(x)
        if like == 0:
            like = 0
        else:
            like = like_Regressor.predict(x).tolist()[0]
        toWrite = items[0] + '\t' + items[1] + '\t' + str(int(forward)) + ',' + str(int(comment)) + ',' + str(int(like)) + '\n'
        fw.write(toWrite)
finally:
    if fr:
        fr.close()
    if fw:
        fw.close()