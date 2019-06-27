# 求 1到50之间的奇数和
def sum_demo():
    sum = 0
    for i in range(1, 51):
        if i % 2 == 1:
            sum = sum + i
    print(sum)
# 求1到50之间所有数的和
def he():
    sum=0
    for i in range(1,51):
        sum = sum + i
    print(sum)
# 打印九九乘法表
def jiujiu():

    for i in range(1,10):
        x = i+1
        for j in range(1,x):
            print('%s * %s = %s'%(j,i,j*i),end='   ')
        print('')

# 求两个数之间的偶数和
def sum_demo1(a,b):
    sum = 0
    if a<b:
        for i in range(a+1,b):
            if i%2 ==0:
                sum = sum+i
        print(sum)
    elif a>b:
        for i in range(b,a+1):
            if i%2 ==0:
                sum = sum+i
        print(sum)
    else:
        print('a和 b 相等')
#取1-10中间的奇数和
def jishuhe():
    sum = 0
    for k in range(2,10):
        if k%2==1:
            sum=sum+k

    print(sum)


'''
每次拿 4 个 最后剩一个, 
每次拿五个剩四个,
每次拿6个 最后剩3个,
每次拿七个最后剩5个,
每次拿八个最后剩一个,
每次拿九个 刚好拿完, 篮子最多放1000个鸡蛋,求有多少鸡蛋
'''
#自己做
def zijizuo():
    for k in range(1,1000):
        if (k%4==1):
            if (k%5==4):
                if(k%6==3):
                    if(k%7==5):
                        if(k%8==1):
                            if(k%9==0):
                                print(k)

# 篮子拿鸡蛋 1
def jidan():
    for i in range(1, 1000):
        if (i % 4 == 1):
            if (i % 5 == 4):
                if (i % 6 == 3):
                    if (i % 7 == 5):
                        if (i % 8 == 1):
                            if (i % 9 == 0):
                                print(i)
# 篮子拿鸡蛋 2
def jidan2():
    for i in range(1, 1000):
        if i % 4 != 1:
            continue
        if i % 5 != 4:
            continue
        if i % 6 != 3:
            continue
        if i % 7 != 5:
            continue
        if i % 8 != 1:
            continue
        if i % 9 != 0:
            continue
        print(i)


def paixu():
    alist=[12,59,63,1,52,41,30,20,5]
    for i in range(len(alist)-1):
        for k in range(len(alist)-i-1):
            if alist[k]>alist[k+1]:
                temp=alist[k]
                alist[k]=alist[k+1]
                alist[k+1]=temp
    print(alist)

def paixu2():
    A=[5,6,2,0,3,4,8,1]
    for i in range(len(A)-1):
        for j in range(len(A)-i-1):
            if A[j]>A[j+1]:
                B=A[j]
                A[j]=A[j+1]
                A[j+1]=B
    print(A)
def zuoye():
    A = [1, 2, 3, 4, 5]
    print(A[1])
    print(A[1:4])
    A.pop(3)
    print(A)
    B = [6, 7]
    A.extend(B)
    print(A)
    A[0] = '5'
    print(A)
    print(len(A))

def zuoye2():
    A = {'lin':'林','cheng':'成'}
    print(A)
    print(A['lin'])
    A.pop('lin')
    print(A)
    A['yu'] = '禹'
    print(A)
    A['cheng']='C'
    print(A)
    C = {'lin':'L'}
    A.update(C)
    print(A)

def lianxi1():
    for i in range(1,10):
        x = i + 1
        for k in range(1,x):
            print('%s*%s=%s'%(i,k,i*k),end='    ')
        print('')
def list():
    A=[]
    for i in range(2,30):
        if i%3==0:
            A.append(i)
    print(A)
    sum=0
    for k in A:
        sum=sum+k
    print(sum)


if __name__ == '__main__':
    pass
    # list()
    # lianxi1()
    # he()
    # zuoye2()
    # zuoye()
    # sum_demo()
    # jiujiu()
    # sum_demo1(2,10)
    # jishuhe()
    # jidan()
    # jidan2()
    # zijizuo()
    # paixu()
    # paixu2()
    # jjcfb()