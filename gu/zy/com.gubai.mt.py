import parsel
import requests


url = 'http://www.netbian.com/s/chaogaoqing/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

pul = requests.get(url=url,headers=headers)
pul.encoding = 'gbk'
pul_text = pul.text

selector = parsel.Selector(pul_text)
xpa = selector.xpath('//div[@id="main"]/div[3]/ul/li')

for xp in xpa:
    xp1 = xp.xpath('.//a/img/@src').get()
    xp2 = xp.xpath('.//a/b/text()').get()

    for x in xp1:
        img = requests.get(url=x, headers=headers).content

        mm = xp1.split('/')[-1]


        with open(f'img\\'+mm, mode='wb') as f:
            f.write(img)
            print('完成:', mm)