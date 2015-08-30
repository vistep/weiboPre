__author__ = 'Administrator'
# _*_ coding: utf-8 _*_
import codecs

fr = codecs.open('./data/wordVector.txt', mode='r', encoding='utf-8')
fw1 = codecs.open('./data/wordVectorSample1.txt', mode='w', encoding='utf-8')
fw2 = codecs.open('./data/wordVectorSample2.txt', mode='w', encoding='utf-8')
fw3 = codecs.open('./data/wordVectorSample3.txt', mode='w', encoding='utf-8')
fw4 = codecs.open('./data/wordVectorSample4.txt', mode='w', encoding='utf-8')
fw5 = codecs.open('./data/wordVectorSample5.txt', mode='w', encoding='utf-8')
fw6 = codecs.open('./data/wordVectorSample6.txt', mode='w', encoding='utf-8')
fw7 = codecs.open('./data/wordVectorSample7.txt', mode='w', encoding='utf-8')
fw8 = codecs.open('./data/wordVectorSample8.txt', mode='w', encoding='utf-8')

for i in range(0, 200000):
    fw1.write(fr.readline())

for i in range(200000, 400000):
    fw2.write(fr.readline())

for i in range(400000, 600000):
    fw3.write(fr.readline())

for i in range(600000, 800000):
    fw4.write(fr.readline())

for i in range(800000, 1000000):
    fw5.write(fr.readline())

for i in range(1000000, 1200000):
    fw6.write(fr.readline())

for i in range(1200000, 1400000):
    fw7.write(fr.readline())

for i in range(1400000, 1626750):
    fw8.write(fr.readline())

fr.close()
fw1.close()
fw2.close()
fw3.close()
fw4.close()
fw5.close()
fw6.close()
fw7.close()
fw8.close()

