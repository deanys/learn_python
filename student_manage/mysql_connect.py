import pymysql

INSERT_TABLE = "insert into manager (`name`, `sex`, `math`, `english`, `culture`) "
INSERT_ALL_TABLE = "INSERT INTO `manager` (`number`, `name`, `sex`, `math`, `english`, `culture`) "


class Mysql(object):
    def __init__(self):
        print("这是数据库")
        try:
            self.db = pymysql.connect(host="localhost", port=3306, db="student", user="root", passwd="zxcvbnm",
                                      charset="utf8")
            self.conn = self.db.cursor()
        except Exception as e:
            raise "数据库没连接,异常{}".format(e)
        print("数据库已经连接")

    def exec_comand(self, sql):
        try:
            self.conn.execute(sql)
            data = self.conn.fetchall()
            self.db.commit()
            print("insert ok")
            return data
        except Exception:
            print("数据错误")
            self.db.rollback()

    def close_sql(self):
        self.db.close()
        self.conn.close()

    def fetch_all_data(self):
        sql = "select * from manager"
        return self.exec_comand(sql)

    def fetch_one_data(self, name):
        sql = "select * from manager where name=\"{}\"".format(name)
        return self.exec_comand(sql)

    def insert_date_to_sql(self, one_data):
        # INSERT INTO `manager`(`name`, `sex`, `math`, `english`, `culture`) VALUES('杨硕', '男', '150', '150', '150')
        print(one_data, len(one_data))
        if len(one_data) == 5:
            sql = '''{}values("{}","{}","{}","{}","{}")'''.format(INSERT_TABLE, one_data[0], one_data[1],
                                                                  one_data[2], one_data[3], one_data[4])
            print(sql)
        elif len(one_data) == 6:
            sql = '''{}values("{}","{}","{}","{}","{}","{}")'''.format(INSERT_ALL_TABLE, one_data[0], one_data[1],
                                                                       one_data[2], one_data[3], one_data[4],
                                                                       one_data[5])
            print(sql)
        else:
            print("数据格式错误")
            return
        return self.exec_comand(sql)

    def del_date(self, name):
        sql = "delete from manager where name=\"{}\"".format(name)
        print(sql)
        self.exec_comand(sql)

    def update_to_mysql(self, name, filed, update_field, id="name"):
        sql = '''update manager set {}="{}" where {}="{}" '''.format(filed, update_field, id, name)
        return self.exec_comand(sql)


'''

s = Mysql()
s.fetch_all_data()
s.fetch_one_data("赵玉")
data = [["二狗", "男", "100", "89", "79"], ["123", "小子", "男", "100", "89", "79"]]
s.insert_date_to_sql(data)
s.del_date("二狗")
s.update_to_mysql("number", "4", "name", "小子")
s.close_sql()
'''
