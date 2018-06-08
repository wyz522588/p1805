user = input('请输入您的性别:')
if user == '男':
    shen=int(input('请输入您的身高：'))
    caifu=int(input('你有多少钱？'))
    yanzhi=int(input('请输入您的颜值'))
    if shen>=180 and caifu >=1000 and yanzhi >= 90:
        print('#'*50)
        print('标准的高富帅')
    else:
        print('#'*50)
        print('屌丝一个')

if user == '女':
    shen=input('请输入您的肤色：')
    caifu=int(input('你有多少钱？'))
    yanzhi=int(input('请输入您的颜值'))
    if shen == "白色" and caifu >=800 and yanzhi >= 90:
        print('*'*50)
        print('标准的白富美')
    else:
        print('*'*50)
        print('女屌丝一枚')
