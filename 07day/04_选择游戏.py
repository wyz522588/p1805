print('请选择您要玩的游戏')
a = input('1.王者荣耀  2，贪玩蓝月:')
b=123
c=456
if a == '1':
    zhang = int(input('请输入账号:'))
    mima = int(input('请输入密码：'))
    if zhang == b and mima == c:
        print('欢迎来到王者峡谷')
    else:
        print('密码错误')
if a == '2':
    print('欢迎来到贪玩登录主页')
    zhang = int(input('请输入账号'))
    mima = int(input('请输入密码'))
    if zhang == b and mima == c:
        print('欢迎来到贪玩蓝月，我是渣渣灰')
    else:
        print('登录失败')

