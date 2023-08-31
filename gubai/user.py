import pymysql

conn = pymysql.connect(host='192.168.233.200', port=3306, database='gubai', user='root', password='102030',charset='utf8')
csl = conn.cursor()

def user1():
    sql = "SELECT`user`.id,`username`,`password`,`phone`,`mail`,`age`,`sex`,`img`,authority.aut_name,`datetime`,`date` FROM`user`INNER JOIN authority ON authority.user_id = `user`.authority_id ORDER BY authority.aut_name, `user`.username;"
    csl.execute(sql)
    data =csl.fetchall()
    data1 = []
    for data in data:
        i1 = data[-1].strftime('%Y-%m-%d')
        i2 = data[-2].strftime('%Y-%m-%d %H:%M:%S')
        i3 = data[0:8]
        list1 = i3+(i1, i2)
        li = list(list1)
        li1 = lihhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
        print(li1)

# print(user1())
def mysql(q):
    sql = "SELECT * FROM `user` WHERE id = %s;" % q
    csl.execute(sql)
    data = csl.fetchall()
    return data

# mysql(2)
user1()