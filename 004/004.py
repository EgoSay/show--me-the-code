# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/1 下午5:45
# @IDE     : PyCharm
import re
from collections import Counter


def creat_list(filename):
    datalist = []
    with open(filename, 'r') as f:
        for line in f:
            content = re.sub("\"|,|\.", "", line)
            print(content)
            datalist.extend(content.strip().split(' '))
    return datalist


if __name__ == '__main__':
    print(Counter(creat_list('test.txt')))
