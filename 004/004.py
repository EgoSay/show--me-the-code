# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/1 下午5:45
# @IDE     : PyCharm
import re
from collections import Counter
from functools import reduce


def create_list(filename):
    word_list = list()
    with open(filename, 'r') as f:
        # 利用正则表达式，‘\b’匹配一个单词边界，即字与空格间的位置,‘+’等价于匹配长度{1,}
        content = re.findall("\b?([A-Za-z]+)\b?", f.read())
        print(content)
        word_list.extend(content)
    return word_list


if __name__ == '__main__':
    words = Counter(create_list('test.txt'))
    print(reduce(lambda x, y: x + y, words.values()))