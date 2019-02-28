# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/2/28 下午2:53
# @IDE     : PyCharm

import random
import string

# 参考他人的代码将创建mysql类以及将操作的方法封装，规范代码
import pymysql

KEY_LEN = 20
KEY_ALL = 200


def base_str():
    return string.ascii_letters + string.digits


def key_gen():
    key_list = [random.choice(base_str()) for i in range(KEY_LEN)]
    return "".join(key_list)


def key_num(num, result=None):
    if result is None:
        result = []
    for i in range(num):
        result.append(str(key_gen()))
    return result


class InitMysql(object):

    def __init__(self, conn):
        self.conn = None

    # connect to mysql
    def connect(self):
        self.conn = pymysql.connect(
            host='localhost',
            port=32768,
            user='root',
            passwd='Geotmt_123',
            db='test',
            cursorclass=pymysql.cursors.DictCursor
        )

    def cursor(self):
        try:
            return self.conn.cursor()
        except (AttributeError, pymysql.OperationalError):
            self.connect()
            return self.conn.cursor()

    def commit(self):
        return self.conn.commit()

    def close(self):
        return self.conn.close()


def process():
    dbConn.connect()
    conn = dbConn.cursor()
    drop_table(conn)
    create_table(conn)
    insert_data(conn)
    # query_data(conn)
    dbConn.commit()
    dbConn.close()


def query(sql, conn):
    """查询sql"""
    conn.execute(sql)
    rows = conn.fetchall()
    return rows


def drop_table(conn):
    conn.execute("DROP TABLE IF EXISTS `user_key`")


def create_table(conn):
    sql_create = "CREATE TABLE `user_key` \
        (`id` int(11) NOT NULL AUTO_INCREMENT,`code` varchar(255) DEFAULT NULL,PRIMARY KEY (`id`)) \
        ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;"
    conn.execute(sql_create)


def insert_data(conn):
    insert_sql = "INSERT INTO `user_key`(code) VALUES (%s)"
    key_list = key_num(KEY_ALL)
    # print(len(key_list))
    conn.executemany(insert_sql, key_list)


def delete_data(conn):
    del_sql = "delete from user_key where id=2"
    conn.execute(del_sql)


def query_data(conn):
    sql = "select `id`,`code` from `user_key` order by `id`"
    rows = query(sql, conn)
    print_result(rows)


def print_result(rows):
    if rows is None:
        print("rows None")
    for row in rows:
        print(row)


if __name__ == "__main__":
    dbConn = InitMysql(None)
    process()
