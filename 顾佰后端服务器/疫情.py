import requests
import json

from pymysql import connect


url = 'https://c.m.163.com/ug/api/wuhan/app/data/list-total?t=334099496200'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42'
}

reques = requests.get(url=url, headers=headers)
data = reques.json()

def ind():
    ll = data['data']['chinaDayList']
    f = []
    for i in ll:
        # 时间
        ii1 = i['date']
        # 确诊
        ii2 = i['today']['confirm']
        # 累计确诊
        ii4 = i['total']['confirm']
        # 累计治愈
        ii5 = i['total']['heal']
        #累计死亡
        ii6 = i['total']['dead']
        # 现有确诊
        ii8 = i['total']['storeConfirm']
        # print(ii1,ii2,ii4,ii5,ii6,ii8)
        a = []
        a.append([ii1,ii2,ii4,ii5,ii6,ii8])
        conn = connect(host='localhost', port=3306, database='疫情', user='root', password='102030',
                       charset='utf8')
        csl = conn.cursor()

        n = 1
        for jkh in a:
            try:
                csl.execute('INSERT INTO date(`时间`,`确诊`,`累计确诊`,`累计治愈`,`累计死亡`,`现有确诊`) VALUES(%s,%s,%s,%s,%s,%s) on DUPLICATE key UPDATE 时间=VALUES(时间);',
                            (jkh[0],jkh[1], jkh[2], jkh[3], jkh[4], jkh[5]))

                conn.commit()
            except Exception as e:
                conn.rollback()# 游标
                print('第'+ str(n)+'错误')
                n +=1

        conn.close()
        csl.close()
        print('完成')

def ind1():
    ll = data['data']['areaTree']
    for i in ll:
        # 国家
        ii0 = i['name']
        # id
        ii1 = i['id']
        # 新增确诊
        ii2 = i['today']['confirm']
        # 累计确诊
        ii3 = i['total']['confirm']
        # 死亡
        ii4 = i['total']['dead']
        # 治愈
        ii5 = i['total']['heal']
        # print(ii1,ii0,ii2, ii3, ii4, ii5)
        a = []
        a.append([ii1,ii0,ii2, ii3, ii4, ii5])
        conn = connect(host='localhost', port=3306, database='疫情', user='root', password='102030',
                       charset='utf8')
        csl = conn.cursor()

        n = 1
        for jkh in a:
            try:
                csl.execute('INSERT INTO `国家`(id,`国家`,`新增确诊`,`累计确诊`,`死亡`,`治愈`) VALUES(%s,%s,%s,%s,%s,%s);', (jkh[0], jkh[1], jkh[2], jkh[3], jkh[4], jkh[5]))

                conn.commit()
            except Exception as e:
                conn.rollback()  # 游标
                print('第' + str(n) + '错误')
                n += 1

        conn.close()
        csl.close()
        print('完成')
# ind1()
def ind2():
    ll = data['data']['areaTree']
    for i in ll:
        ii1 = i['children']
        # print(ii0)
        for ii in ii1:
            # 名字
            ii2 = ii['name']
            # id
            ii3 = ii['id']
            # 时间
            ii4 = ii['lastUpdateTime']
            # 昨日新增
            ii5 = ii['today']['confirm']
            # 确诊
            ii6 = ii['total']['confirm']
            # 死亡
            ii7 = ii['total']['dead']
            # 治愈
            ii8 = ii['total']['heal']
            # print(ii3, ii2, ii4, ii5, ii6, ii7, ii8)
            a = []
            a.append([ii3, ii2, ii4, ii5, ii6, ii7, ii8])
            conn = connect(host='localhost', port=3306, database='疫情', user='root', password='102030',
                           charset='utf8')
            csl = conn.cursor()

            n = 1
            for jkh in a:
                try:
                    csl.execute('INSERT INTO date(`时间`,`确诊`,`累计确诊`,`累计治愈`,`累计死亡`,`现有确诊`) VALUES(%s,%s,%s,%s,%s,%s) on DUPLICATE key UPDATE 时间=VALUES(时间);',
                        (jkh[0], jkh[1], jkh[2], jkh[3], jkh[4], jkh[5]))

                    conn.commit()
                except Exception as e:
                    conn.rollback()  # 游标
                    print('第' + str(n) + '错误')
                    n += 1

            conn.close()
            csl.close()
            print('完成')









