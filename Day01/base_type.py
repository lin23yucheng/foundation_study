
# 整数类型
def fangfa_1():
    lin = 23
    print(type(lin))
# 字符串类型
def fangfa_2():
    cheng = '23'
    print(type(cheng))
# 浮点型
def fangfa_3():
    yu = 3.1415926
    print(type(yu))
# 转换
def zhuanhuan():
    linyucheng = 3.14
    print(type( int(linyucheng) ))
def def1():
    print('def1')

def def2():
    print('def2')

def def3():
    print('def3')

def jiehe():
    lin = 3.14
    yu = 'π'
    cheng = '等于'
    print('%s%s%s'%(yu,cheng,lin))

def add(no1,no2):
    print(no1)
    print(no2)
    print(no1 + no2)
    return no1+no2


if __name__ == '__main__':
    print('Hello world')
    # fangfa_1()
    # fangfa_2()
    # fangfa_3()
    # def3()
    # def1()
    # def2()
    # zhuanhuan()
    # jiehe()
    b = add(20, 80)
    print('----------')
    print(b)
    a = ('语法错误无效语法')
    print(a[0:4])
    print(a[::-1])
