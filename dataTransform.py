__author__ = 'Administrator'
# _*_ coding: utf-8 _*_
import codecs
import numpy as np

def transform(parseArr):
    print parseArr
    length = np.size(parseArr)
    arr = [0] * 1000
    for i in range(0, length, 2):
        arr[parseArr[i]] = parseArr[i + 1]
    return arr


fr = codecs.open('./data/word2vec.txt', mode='r', encoding='utf-8')
fw = codecs.open('./data/wordVector.txt', mode='w', encoding='utf-8')
try:
    while True:
        text = fr.readline()
        if not text:
            break
        items = text.split('\t')
        if len(items[1]) < 2:
            fw.write(text)
            continue
        parse = np.fromstring(items[1], dtype=int, sep=' ')
        arr1000 = transform(parse)
        fw.write(items[0] + '\t' + str(arr1000)[1:-1] + '\n')
finally:
    if fr:
        fr.close()
    if fw:
        fw.close()
