__author__ = 'Administrator'
# _*_ coding: utf-8 _*_
import codecs

for name in ['forward', 'comment', 'like']:
    readfile1 = './data/train_' + name + '_0or1.txt'
    readfile2 = './data/train_' + name + '_notZero.txt'
    writeDir1 = './data/train_' + name + '_0or1/'
    writeDir2 = './data/train_' + name + '_notZero/'
    fr1 = codecs.open(readfile1, mode='r', encoding='utf-8')
    fr2 = codecs.open(readfile2, mode='r', encoding='utf-8')
    fw1X = codecs.open(writeDir1 + 'x.txt', mode='w', encoding='utf-8')
    fw1Y = codecs.open(writeDir1 + 'y.txt', mode='w', encoding='utf-8')
    fw2X = codecs.open(writeDir2 + 'x.txt', mode='w', encoding='utf-8')
    fw2Y = codecs.open(writeDir2 + 'y.txt', mode='w', encoding='utf-8')
    try:
        while True:
            text = fr1.readline()
            if not text:
                break
            items = text.split('\t')
            x = items[-1][1:-2]
            y = items[-2]
            fw1X.write(x + '\n')
            fw1Y.write(y + '\n')
        while True:
            text = fr2.readline()
            if not text:
                break
            items = text.split('\t')
            x = items[-1][1:-2]
            y = items[-2]
            fw2X.write(x + '\n')
            fw2Y.write(y + '\n')
    finally:
        if fr1:
            fr1.close()
        if fr2:
            fr2.close()
        if fw1X:
            fw1X.close()
        if fw1Y:
            fw1Y.close()
        if fw2X:
            fw2X.close()
        if fw2Y:
            fw2Y.close()

