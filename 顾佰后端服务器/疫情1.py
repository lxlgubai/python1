import requests

url = 'https://c.m.163.com/ug/api/wuhan/app/data/list-total?t=334099496200'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42'
}

reques = requests.get(url=url, headers=headers)
data = reques.json()


def ind():
    ll = data['data']['chinaDayList']
    a5 = []
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

        a1 = {'时间': ii1, '确诊': ii2, '累计确诊': ii4, '累计治愈': ii5, '累计死亡': ii6, '现有确诊': ii8}

        a5.append(a1)
    return a5

def ind1():
    ll = data['data']['areaTree']
    a5 = []
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
        a1 = {'id': ii1, '国家': ii0, '新增确诊': ii2, '累计确诊': ii3, '死亡': ii4, '治愈': ii5}
        a5.append(a1)
    return a5

# ind1()
def ind2():
    ll = data['data']['areaTree']
    a5 = []
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
            a1 = {'id': ii3, '名字': ii2, '时间': ii4, '昨日新增': ii5, '确诊': ii6, '死亡': ii7, '治愈': ii8}

            a5.append(a1)
    return a5


