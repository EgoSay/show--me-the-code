# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/2/27 下午6:21
# @IDE     : PyCharm

"""
主要学习了random模块的使用
    random() 返回0<=n<1之间的随机实数n；
    choice(seq) 从序列seq中返回随机的元素；
    getrandbits(n) 以长整型形式返回n个随机位；
    shuffle(seq[, random]) 原地指定seq序列；
    sample(seq, n) 从序列seq中选择n个随机且独立的元素
"""
import random

code_list = []
# 生成26个大写的字母
for x in range(65, 91):
    a = str(chr(x))  # 生成对应的ASCII码对应的字符串
    code_list.append(a)
# 生成26个小写字母
for x in range(97, 123):
    a = str(chr(x))  # 生成对应的ASCII码
    code_list.append(a)
# 生成10个数字
for x in range(10):
    code_list.append(str(x))


def gen_code():  # 生成16位验证码
    code = ""
    for index in range(16):
        code += random.choice(code_list)

    print(code)


# 生成200个验证码
for i in range(200):
    gen_code()
