# @Author  : adairchan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/4/21 11:40
# @IDE     : PyCharm


import glob
from collections import Counter
import re


def list_txt():
    return glob.glob("*.txt")


def wc(filename):
    word_list = list()
    with open(filename, 'r') as f:
        for line in f:
            content = re.sub("\"|,|\.|!|\?", "", line)    # 正则将, . ! ?等句子标点符号去掉，相当于只保留单词
            word_list.extend(content.strip().split(' '))
    # Counter统计单词
    return Counter(word_list).most_common(1)


if __name__ == "__main__":
    # most_comm()
    for li in list_txt():
        print("文件{}中最重要的单词统计:{}".format(li, wc(li)))


