__author__ = 'Administrator'
# _*_ coding: utf-8 _*_

import codecs
fr = codecs.open("./data/train_feature.txt", mode='r', encoding='utf-8')
fw_forward1 = codecs.open("./data/train_forward_0or1.txt", mode='w', encoding='utf-8')
fw_forward2 = codecs.open("./data/train_forward_notZero.txt", mode='w', encoding='utf-8')
fw_comment1 = codecs.open("./data/train_comment_0or1.txt", mode='w', encoding='utf-8')
fw_comment2 = codecs.open("./data/train_comment_notZero.txt", mode='w', encoding='utf-8')
fw_like1 = codecs.open("./data/train_like_0or1.txt", mode='w', encoding='utf-8')
fw_like2 = codecs.open("./data/train_like_notZero.txt", mode='w', encoding='utf-8')
try:
    while True:
        text = fr.readline()
        if not text:
            break
        items = text.split('\t')

        indicator = u'0' if items[3] == u'0' else u'1'
        forward1 = items[0] + '\t' + items[1] + '\t' + items[2] + '\t' + indicator + '\t' + items[-1]
        fw_forward1.write(forward1)
        if indicator == u'1':
            forward2 = items[0] + '\t' + items[1] + '\t' + items[2] + '\t' + items[3] + '\t' + items[-1]
            fw_forward2.write(forward2)

        indicator = u'0' if items[4] == u'0' else u'1'
        comment1 = items[0] + '\t' + items[1] + '\t' + items[2] + '\t' + indicator + '\t' + items[-1]
        fw_comment1.write(comment1)
        if indicator == u'1':
            comment2 = items[0] + '\t' + items[1] + '\t' + items[2] + '\t' + items[4] + '\t' + items[-1]
            fw_comment2.write(comment2)

        indicator = u'0' if items[5] == u'0' else u'1'
        like1 = items[0] + '\t' + items[1] + '\t' + items[2] + '\t' + indicator + '\t' + items[-1]
        fw_like1.write(like1)
        if indicator == u'1':
            like2 = items[0] + '\t' + items[1] + '\t' + items[2] + '\t' + items[5] + '\t' + items[-1]
            fw_like2.write(like2)
finally:
    if not fw_forward1:
        fw_forward1.close()
    if not fw_forward2:
        fw_forward2.close()
    if not fw_comment1:
        fw_comment1.close()
    if not fw_comment2:
        fw_comment2.close()
    if not fw_like1:
        fw_like1.close()
    if not fw_like2:
        fw_like2.close()
