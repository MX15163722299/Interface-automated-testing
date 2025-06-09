# common/mysql_client.py
import pymysql
from common.read_config import ReadConfig  # 你自己写的类

class MySQLClient:
    def __init__(self):
        self.host = ReadConfig().get_config("mysql","host")
        self.port = ReadConfig().get_config("mysql","port")
        self.user = ReadConfig().get_config("mysql", "user")
        self.pwd = ReadConfig().get_config("mysql", "pwd")
        self.database = ReadConfig().get_config("mysql", "database")
        self.charset = ReadConfig().get_config("mysql", "charset")
        self.conn = pymysql.connect(
            host = self.host,
            port = int(self.port),
            user = self.user,
            password = self.pwd,
            database = self.database,  # 改成你实际数据库名
            charset = self.charset
        )
        self.cursor = self.conn.cursor()

    def query(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def execute(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    mysql = MySQLClient()
    print(mysql.query("select name from rental_survey where id = 30"))
    mysql.close()