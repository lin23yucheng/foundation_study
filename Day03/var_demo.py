
vavr = '你好'

def d1():
    print(vavr)
    bvavr='哈哈'
def d2():
    print(bvavr)#会报错,bvavr不是全局变量
def d3():
    global vavr
    vavr='嗯嗯'

if __name__ == '__main__':
    d1()
    d3()
    d1()
