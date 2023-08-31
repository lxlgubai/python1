import requests



url = 'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=&city=100010000&experience=&degree=&industry=&scale=&stage=&position=100101&salary=&multiBusinessDistrict=&page=1&pageSize=30'

headers = {
    'sec-ch-ua-platform': 'Windows',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
'name': 'af570efa', 'seed': '7Zrd1+sFrDJzNwX1PYSHYadvwEyHuFQMeNfo3Rp2r40=',
    'Host': 'www.zhipin.com',
    'Referer': 'https://www.zhipin.com/web/geek/job?query=',
    'cookie': 'lastCity=101020100; wd_guid=b3fad9a5-6b8e-4c60-92f7-afe91b52a16b; historyState=state; _bl_uid=ydlRIbjzh8gtjI4mz8I0p9e5pCs8; __zp_stoken__=63faeKWp6FTJ%2FPAVmZSRILx5xeHI1Azc9bDwIGRFXaGpCSBlpI20%2BUxhvFn9CPUx0LXZ0L0RlEkAmKCY3FFJBew1sLH91I1lXGl1QeCgmFE12ETBAViFhXwh4RCoJXys%2Fb09GTjVsEDw4Onw%3D',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46'
}

html_requests = requests.get(url=url, headers=headers)
gg = html_requests.json()
print(gg)

# json_gob = html_json['zpData']['jobList']
# print(json_gob)
# for gon in json_gob:
#     gon1 = gon['areaDistrict']
#     gon2 = gon['bossAvatar']
#     gon3 = gon['bossName']
#     gon4 = gon['bossTitle']
#     gon5 = gon['brandIndustry']
#     gon6 = gon['brandLogo']
#     gon7 = gon['brandName']
#     gon8 = gon['brandScaleName']
#     gon9 = gon['brandScaleName']
#     gon10 = gon['brandStageName']
#     gon11 = gon['businessDistrict']
#     gon12 = gon['cityName']
#     gon13 = gon['jobDegree']
#     gon14 = gon['jobExperience']
#     gon15 = gon['jobName']
#     gon16 = gon['salaryDesc']
#     gon17 = gon['skills']
#     gon18 = gon['welfareList']
#     print(gon1,
#     gon2,
#     gon3,
#     gon4,
#     gon5,
#     gon6,
#     gon7,
#     gon8,
#     gon9,
#     gon10,
#     gon11,
#     gon12,
#     gon13,
#     gon14,
#     gon15,
#     gon16,
#     gon17,
#     gon18 )

