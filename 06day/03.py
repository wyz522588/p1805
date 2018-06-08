a=int(input('请输入年份:'))
b=2
c=a%b
a=366*24*60*60
b=365*24*60*60
if c == 0:
    print('一共有%d秒'%a)
else:
    print('一共有%d秒'%b)
