# 导包
import requests
import parsel
import os

# 网站地址
url = 'https://qulingyu6.com/lingyu/miaoxiezhen/'

# 隐藏自己
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
html_str = response.text
# print(html_str)

selector = parsel.Selector(html_str)

lis = selector.xpath('//div[@class="update_area_content"]/ul/li')

for li in lis:
    pic_title = li.xpath('.//div[@class="case_info"]/a/text()').get()
    pic_url = li.xpath('.//div[@class="case_info"]/a/@href').get()
    print(pic_title)

    if not os.path.exists('img\\' + pic_title):
        os.mkdir('img\\' + pic_title)

    response_pic = requests.get(url=pic_url, headers=headers).text

    selector_2 = parsel.Selector(response_pic)
    pic_url_list = selector_2.xpath('//div[@id="content"]/figure/a/@href').getall()
    # print(pic_url_list)

    for pic_url in pic_url_list:
        img_data = requests.get(url=pic_url, headers=headers).content
        print(img_data)
        # file_name = pic_url.split('/')[-1]
        # # print(file_name)
        #
        # with open(f'img\\'+ file_name, mode='wb') as f:
        #     f.write(img_data)
        #     print('完成:', file_name)
