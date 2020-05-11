import pymysql

config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'jianghua521',
          'db':'python-db',
          'charset':'utf8mb4',
          'cursorclass':pymysql.cursors.DictCursor,
          }

conn = pymysql.connect(**config)

SQL_CREATE_TABLE = "create table 'test' (" \
                   " 'id' int(11) NOT NULL AUTO_INCREMENT", \
                   " 'name' varchar(50) DEFAULT NULL" \
                   " PRIMARY KEY ('id') " \
                   ")"

SQL_QUERY_ALL = "select * from test"


# 执行sql
def __execute(sql):
    try:
        with conn.cursor() as cursor:
            # sql = "insert into college_student(id,name,age,major) values(%s, %s, %s, %s)"
            cursor.execute(sql, (1, "jwy", 26, "javaaaaaa"))
            # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
            conn.commit()
    finally:
        conn.close()

if __name__ == '__main__':
    __execute("create table test(int id)")