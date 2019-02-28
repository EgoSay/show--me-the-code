# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/2/27 下午6:43
# @IDE     : PyCharm

"""
熟悉了mysql数据库的相关操作
思考：如何实现百万数据有限时间内插入数据库
思路: 利用事务 + 批处理的方式
"""
import random
import string
import time

import pymysql

code_list = list()
db = pymysql.connect(
    host='localhost',
    port=32768,
    user='root',
    passwd='Geotmt_123',
    db='test',
    cursorclass=pymysql.cursors.DictCursor
)


# # 生成26个大写的字母
# for x in range(65, 91):
#     a = str(chr(x))  # 生成对应的ASCII码对应的字符串
#     chars.append(a)
# # 生成26个小写字母
# for x in range(97, 123):
#     a = str(chr(x))  # 生成对应的ASCII码
#     chars.append(a)
# # 生成10个数字
# for x in range(10):
#     chars.append(str(x))


# 发现string类里面已经有对应的字符类型串
def base_str():
    return string.ascii_letters + string.digits


def gen_code():  # 生成16位验证码
    code = [random.choice(base_str()) for i in range(16)]
    return "".join(code)


def insert():
    with db.cursor() as cursor:
        sql = "INSERT INTO code(code) values (%s)"
        cursor.executemany(sql, code_list)
    db.commit()


start = time.perf_counter()
# 生成200个验证码
for i in range(200):
    gen_code()

insert()
end = time.perf_counter()
print('[insert_by_loop execute] Time Usage:', end - start)
