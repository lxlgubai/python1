# ac = input('请输入身份证')
# a = ac.strip()
# if len(a) == 18:
#     if a[0:17].isdigit() and "True":
#         print('身份证输入正确')
#     else:
#         print('请查看身份证中间有误：' + a)
# else:
#     print('请输入正确的身份证号码')

aa = int(input('请输入购物金额'))
vip = input('是否是VIP会员 y/n')
if aa >= 5000:
    print("ss1", aa*0.7)
elif aa >= 2000:
    print("ss2", aa*0.8)
elif aa >= 1000:
    print("ss3", aa*0.9)
else:
    print('余额不足不能优惠哦 ' , aa)
if vip == "y" or vip == "Y":
    if aa >= 3000:
        print('sss', aa*0.95-50)
    else:
        print('ssss', aa*0.95)
else:
    print('没有优惠哦,你的余额为：{}'% aa)
