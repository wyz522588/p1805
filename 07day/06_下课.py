user = int(input('请输入星期几:'))
if user == 1 or user == 2 or user == 3 or user == 4 or user == 5:
    a = input('请输入上午或下午：')
    if a == '上午':
        shijian = int(input('请输入时间：'))
        if shijian >= 8 and shijian < 10:
            print('*'*50)
            print('孩子正在上课')
        elif shijian >10 and shijian <=12:
            print('*'*50)
            print('孩子正在玩游戏')
    if a == '下午':
        shijian = int(input('请输入时间：'))
        if shijian > 14 and shijian <16:
            print('*'*50)
            pritn('孩子正在上课')
        else:
            print('*'*50)
            print('不知道孩子在干什么')
if user == 6:
    print('*'*50)
    print('全天上课')
elif user ==7:
    print('*'*50)
    print('全体逛街')
