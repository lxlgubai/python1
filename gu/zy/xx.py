import re

import requests
import json

# ps = 10
url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20'
headers= {
    'cookie': 'viewed="6529833"; bid=1_RMZUnPw1c; gr_user_id=771a6e80-638a-4ed5-96eb-aece55bb3a10; ll="118347"; ap_v=0,6.0; ct=y',
    'referer': 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56'
}
reques = requests.get(url=url,headers=headers,timeout=18)
ls = reques.json()
print(ls)
# ll = ls['rank']
for i in ls:
    print(i['title'])
    print(i['rank'])
# for i in ll:
#     ii = i['name']
#     ii1 = i['leaduwer']
#     ii2 = i['actissqty']
#     ii3 = i['onl_subcode']
#     ii4 = i['onl_distr_date']
#     print(ii,ii1,ii2,ii3,ii4)




