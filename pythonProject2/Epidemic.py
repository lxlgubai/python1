import csv
import json
import requests


url = 'https://c.m.163.com/ug/api/wuhan/app/data/list-total?t=334099496200'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42'
}

reques = requests.get(url=url, headers=headers)
data = reques.json()

p1 = []
p2 = []
p3 = []
# p4 = []

def ind():
    ll = data['data']['chinaDayList']
    for i in ll:
        # 时间
        ii1 = i['date']
        # 确诊
        ii2 = i['today']['confirm']
        # 累计确诊
        ii4 = i['total']['confirm']
        # 累计治愈
        ii5 = i['total']['heal']
        # 累计死亡
        ii6 = i['total']['dead']
        # 现有确诊
        ii8 = i['total']['storeConfirm']
        # print(ii1,ii2,ii4,ii5,ii6,ii8)

        a1 = {'date': ii1, 'Confirm': ii2, 'Confirm1': ii4, 'Cure': ii5, 'Cure1': ii6, 'Confirm2': ii8}
        p1.append(a1)

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
        # print(ii1, ii0, ii2, ii3, ii4, ii5)
        a1 = {'id': ii1, 'Country': ii0, 'Confirm': ii2, 'Confirm1': ii3, 'Die': ii4, 'Cure': ii5}
        p2.append(a1)

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
            a1 = {'id': ii3, 'Nameprovince': ii2, 'date': ii4, 'New': ii5, 'Confirm': ii6, 'Die': ii7, 'Cure': ii8}
            p3.append(a1)

def ind3():

    # 无症状感染者
    ll1 = data['data']['chinaTotal']['extData']['noSymptom']
    # 无症状感染者+较昨日
    ll2 = data['data']['chinaTotal']['extData']['incrNoSymptom']
    # 累计确诊
    ll3 = data['data']['chinaTotal']['total']['confirm']
    # 累计确诊+较昨日
    ll4 = data['data']['chinaTotal']['today']['confirm']
    # 境外输入
    ll5 = data['data']['chinaTotal']['total']['input']
    # 境外输入+较昨日
    ll6 = data['data']['chinaTotal']['today']['input']
    # 现有确诊
    # ll7 = data['data']['chinaTotal']['extData']['incrNoSymptom']
    # 现有确诊+较昨日
    ll8 = data['data']['chinaTotal']['today']['storeConfirm']
    # 累计死亡
    ll9 = data['data']['chinaTotal']['total']['dead']
    # 累计死亡+较昨日
    ll10 = data['data']['chinaTotal']['today']['dead']
    # 累计治愈
    ll11 = data['data']['chinaTotal']['total']['heal']
    # 累计治愈+较昨日
    ll12 = data['data']['chinaTotal']['today']['heal']


    llp = data['data']['chinaDayList']
    pp = []
    for llo in llp:
        pp1 = llo['total']['storeConfirm']
        pp.append(pp1)
    # 现有确诊
    ll7 = pp[-1]
    #
    # dds2 = ll1, ll2, ll3, ll4, ll5, ll6, ll7, ll8, ll9, ll10, ll11, ll12
    # print(dds2)
    a1 = {'asymptomati':ll1, 'asymptomatiYesteray':ll2, 'Confirm':ll3,
            'ConfirmYesteray':ll4, 'Outside':ll5, 'OutsideYesteray':ll6, 'Confirm1':ll7,
            'ConfirmYesteray1':ll8, 'Die':ll9, 'DieYesteray':ll10, 'Cure':ll11, 'CureYesteray':ll12}
    return a1


ind()
ind2()
ind1()
p4 = ind3()

def main():
    b5 = {'Date': p1, 'Cointry': p2, 'Cointry1': p3, 'Province': p4}
    return b5
# print(b5)
# print(b5)
# json_data = json.dumps(b5, ensure_ascii=False, indent=2)
# print(json_data)
# with open('ind5.json', 'w', encoding='utf-8') as f:
#     f.write(json_data)