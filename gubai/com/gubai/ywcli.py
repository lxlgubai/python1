from gubai.user import mysql

def __init__():
    pass

def dl():
    ss = input()
    ss = mysql(ss)
    return ss

print(dl())