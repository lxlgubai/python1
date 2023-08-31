import os;

# 获取当前工作路径
print(os.getcwd())

# 创建文件夹
mydir = 'testch14'
if os.path.exists(mydir):
    print("文件已存在 %s" % mydir)
else:
    os.mkdir(mydir)
    print("创建 %s 文件成功" % mydir)