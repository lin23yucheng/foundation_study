
# 运算符
def yunsuan(a,b,c):
    a+=b# a = a + b
    print(a)
    a-=c# a = a - c
    print(a)
    b%=c# b = b%c
    print(b)
    a/=b# a = a/b
    print(a)

if __name__ == '__main__':
    yunsuan(8,10,3)
