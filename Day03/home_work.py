# 求 1到50之间的奇数和
def sum_demo():
    sum = 0
    for i in range(1, 51):
        if i % 2 == 1:
            sum = sum + i
    print(sum)

# 打印九九乘法表
def jiujiu():

    for i in range(1,10):
        x = i+1
        for j in range(1,x):
            print('%s * %s = %s'%(j,i,j*i),end='   ')
            print()
        print('')

if __name__ == '__main__':
    sum_demo()
    jiujiu()