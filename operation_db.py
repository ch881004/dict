"""
数据库操作模块
思路：
将数据库操作封装为一个类，将dict_server需要的数据库操作功能分别写成方法，
在dict_server中实例化对象，需要什么方法直接调用
"""
import pymysql


class Database:
    def __init__(self, host="localhost",
                 port=3306,
                 user="root",
                 passwd="123456",
                 charset="utf8",
                 database=None):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.charset = charset
        self.database = database
        self.connect_database()  # 连接数据库

    # 连接数据库
    def connect_database(self):
        self.db = pymysql.connect(host=self.host,
                                  port=self.port,
                                  user=self.user,
                                  passwd=self.passwd,
                                  charset=self.charset,
                                  database=self.database)

    # 关闭
    def close(self):
        self.db.close()

    # 创建游标
    def create_cursor(self):
        self.cur = self.db.cursor()

    def register(self, name, passwd):
        check = False
        sql = "select * from user where name='%s'" % name
        self.cur.execute(sql)
        r = self.cur.fetchone()
        # print("测试：", r)
        # 查找到则用户存在
        if r:
            return check
        # 插入数据库
        try:
            sql = "insert into user (name,password) VALUES (%s,%s);"
            self.cur.execute(sql, [name, passwd])
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print('插入数据失败,msg=[{}]'.format(e))
        else:
            print('注册成功')
            check = True
        finally:
            return check
