import os,stat
import urllib.request

img_url="https://www.canva.cn/photos/" \
        "d44&imgtype=jpg&er=1&src=http%3A%2F%2Fupload.qianhuaweb.com%2F2017%2F0718%2F1500369506683.jpg"
file_path='D:/book/img'
file_name ="pyt"

try:
    #是否有这个路径
    if not os.path.exists(file_path):
    #创建路径
        os.makedirs(file_path)
        #获得图片后缀
    file_suffix = os.path.splitext(img_url)[1]
    print(file_suffix)
        #拼接图片名（包含路径）
    filename = '{}{}{}{}'.format(file_path,os.sep,file_name,file_suffix)
    print(filename)
       #下载图片，并保存到文件夹中
    urllib.request.urlretrieve(img_url,filename=filename)

except IOError as e:
    print("IOError")
except Exception as e:
    print("Exception")