import os

if __name__ == '__main__':
    # 获取当前目录/路径
    a=os.getcwd()
    print(a)
    #获取上级目录的字符串
    b=os.path.abspath('..')
    print(b)
    #获取上上级目录的字符串
    c=os.path.abspath('../..')
    print(c)
