# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/2/28 下午2:53
# @IDE     : PyCharm

import MySQLdb
import string
import random

KEY_LEN = 20
KEY_ALL = 200


def base_str():
    return string.letters + string.digits


def key_gen():
    keylist = [random.choice(base_str()) for i in range(KEY_LEN)]
    return "".join(keylist)


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
        self.conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user="root",
            passwd="123456",
            db="test",
            charset="utf8"
        )

    def cursor(self):
        try:
            return self.conn.cursor()
        except (AttributeError, MySQLdb.OperationalError):
            self.connect()
            return self.conn.cursor()

    def commit(self):
        return self.conn.commit()

    def close(self):
        return self.conn.close()


def process():
    dbconn.connect()
    conn = dbconn.cursor()
    DropTable(conn)
    CreateTable(conn)
    InsertDatas(conn)
    QueryData(conn)
    dbconn.close()

# def execute(sql):
#     '''执行sql'''
#     conn=dbconn.cursor()
#     conn.execute(sql)

# def executemany(sql, tmp):
#     '''插入多条数据'''
#     conn=dbconn.cursor()
#     conn.executemany(sql,tmp)


def query(sql, conn):
    '''查询sql'''
    # conn=dbconn.cursor()
    conn.execute(sql)
    rows = conn.fetchall()
    return rows


def DropTable(conn):
    # conn=dbconn.cursor()
    conn.execute("DROP TABLE IF EXISTS `user_key`")


def create_table(conn):
    # conn=dbconn.cursor()
    sql_create = ''' CREATE TABLE `user_key` (`key` varchar(50) NOT NULL)'''
    conn.execute(sql_create)


def insert_datas(conn):
    # conn=dbconn.cursor()
    # insert_sql = "insert into user_key values(%s)"
    insert_sql = "INSERT INTO user_key VALUES (%(value)s)"
    key_list = key_num(KEY_ALL)
    # print len(key_list)
    # conn.executemany(insert_sql,str(key_listi))
    # conn.executemany("INSERT INTO user_key VALUES (%(value)s)",
    #                   [dict(value=v) for v in key_list])
    conn.executemany(insert_sql, [dict(value=v) for v in key_list])


def delete_data(conn):
    del_sql = "delete from user_key where id=2"
    conn.execute(del_sql)


def query_data(conn):
    sql = "select * from user_key"
    rows = query(sql, conn)
    print_result(rows)


def print_result(rows):
    if rows is None:
        print("rows None")
    for row in rows:
        print(row)


if __name__ == "__main__":
    dbconn = InitMysql(None)
    process()
