from 顾佰后端服务器.疫情1 import ind, ind2
from flask import Flask


def main():
    ad = ind()
    ad1 = ad[0]

    print(ad1)
    a = []
    for af in ad1:
        a.append(af)
    print(a)
    for aq in ad:

        aw = aq['时间']
        print(aw)

if __name__ == '__main__':
    main()