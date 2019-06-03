class lol(object):

    def __init__(self,name,role,position):
        self.name = name
        self.role = role
        self.position = position

    def play(self):
        print(self.name+'红BUFF')

    def lu(self):
        print(self.name+'远古巨龙')

    def info(self):
        print('英雄:%s,定位:%s,位置:%s'%(self.name,self.role,self.position))
        self.play()

class lolo(lol):
    def __init__(self, name, role, position,sex):
        self.name = name
        self.role = role
        self.position = position
        self.sex = sex

    def lu(self):
        print(self.name+'在磕药')

    def do_test(self):
        print(self.name+'在点塔')
        self.play()

if __name__ == '__main__':
    # lin=lol('凯隐','战士','打野')
    # lin.play()
    # lin.lu()
    # lin.info()
    # print(lin.position)
    yu=lolo('锐雯','战士','上单','妹子')
    yu.lu()
    yu.do_test()
