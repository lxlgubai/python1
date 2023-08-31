import logging
from pymysql import connect

def celetd(sqlstr):
    '''数据库2'''
    conn = connect(host='localhost', port=3306, database='name2', user='root', password='102030', charset='utf8')
    csl = conn.cursor()
    try:
        csl.execute(sqlstr)
        conn.commit()
        return csl.fetchall()

    except Exception as e:
        logging.exception(e)
        conn.rollback()
    conn.close()
    csl.close()