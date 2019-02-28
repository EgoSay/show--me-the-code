# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/2/28 上午10:37
# @IDE     : PyCharm

import string
import random
import redis

CODE_LEN = 20
CODE_ALL = 200


def base_str():
    return string.digits + string.ascii_letters


def key_gen():
    code = [random.choice(base_str()) for i in range(CODE_LEN)]
    return "".join(code)


def key_num(num, result=None):
    if result is None:
        result = []
    for i in range(num):
        result.append(key_gen())
    return result


def redis_init():
    r = redis.Redis(host='localhost', port=36379, db=0)
    return r


def push_to_redis(code_list):
    for code in code_list:
        redis_init().lpush('key', code)


def get_from_redis():
    key_list = redis_init().lrange('key', 0, -1)
    for key in key_list:
        print(key)


if __name__ == "__main__":
    push_to_redis(key_num(CODE_ALL))
    get_from_redis()
