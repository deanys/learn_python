import pymssql

server = "127.0.0.1"
user = "sa"
password = "zxcvbnm"
print("what")
conn = pymssql.connect(server, user, password, "dean")  #获取连接
# print(conn)
if conn is None:
    print("connect error")
else:
    print("econn ok")
cursor = conn.cursor()
cursor.execute("select * from test_name")
print(cursor.fetchall())
