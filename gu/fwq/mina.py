import pymysql

user='root',
password="102030",
host='localhost',
database='name2'
db = pymysql.connect(host,user,password,database)

cursor = db.cursor()
sql = "show databases;"
cursor.execute(sql)

print(cursor)

cursor.close()
db.close()