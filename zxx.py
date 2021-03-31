# coding: utf-8
import jieba
from jieba import posseg as pseg

pos_ = []
print('请输入您需要识别的语句 : （回车键退出）')
# demo_sent = input()
demo_sent = "汤姆喜欢去北京天安门玩"
if demo_sent == '' or demo_sent.isspace():
    print('再见！')
else:
    demo_sent = list(demo_sent.strip())
    print(demo_sent)
    sentence = "".join(demo_sent)
    print(sentence)
    POS = pseg.cut(sentence)
    for w in POS:
        print(w)
        # print(w.word)
        # print(w.flag)
        for i in range(len(w.word)):
            pos_.append(w.flag)
    print(pos_)
    demo_data = [(demo_sent, ['O'] * len(demo_sent), pos_)]
    print(demo_data)

# words = pseg.cut("我爱北京天安门")  # jieba默认模式
# jieba.enable_paddle()  # 启动paddle模式。 0.40版之后开始支持，早期版本不支持
# words = pseg.cut("我爱北京天安门", use_paddle=True)  # paddle模式
# for word, flag in words:
#     print('%s %s' % (word, flag))
