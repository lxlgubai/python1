from pymysql import connect


# conn = connect(host='localhost', port=3306, database='name2', user='root', password='102030', charset='utf8')
# csl = conn.cursor()
#
# csl.execute("CREATE TABLE if not exists `fiction5`(`name` varchar(20) not null,`moods` float(6) not null,`classify` varchar(20) not null,`serialize` varchar(8) not null,`score` float(3) not null,`read`float(4) not null);")
#
# data = csl. fetchall()
#
# conn.close()
# csl.close()

conn = connect(host='localhost', port=3306, database='name2', user='root', password='102030', charset='utf8')
csl = conn.cursor()

csl.execute("SELECT DISTINCT `name` as 书名,`read` as 阅读 FROM fiction1 ORDER BY `read` desc;")

data = csl.fetchall()

print(data)
conn.close()
csl.close()

