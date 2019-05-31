
def open_write():
    text_lin=open('wenjian.txt','w+')
    for yu in range(8):
        text_lin.write('666\n')

def open_write1():
    text_lin = open('wenjian.txt', 'a+')
    text_lin.write('可以')

def open_read():
    text_lin=open('wenjian.txt','r')
    #读取所有行,返回一个list
    # print(text_lin.readlines())
    # 读一行
    print(text_lin.readline())
if __name__ == '__main__':
    # open_write()
    # open_write1()
    open_read()
