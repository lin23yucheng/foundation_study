# 这就是一个列表的数据类型,英文 是 list, 也叫 数组
alist = ['hello',2,'你好',6,7,1,3]
# 访问list
def list_fangfa():
    print(alist[-3])
    print(alist[4:])
# 删除list中的元素
def list_del():
    alist.pop()
    print(alist)
    alist.pop(1)
    print(alist)
    a=alist.pop(1)
    print(a)
# 增加list中的元素
def list_add():
    blist = [2,4,'lin','yu']
    blist.append('cheng')
    print(blist)
# 合并两个list中的元素
    clist = [2,3]
    blist.extend(clist)
    print(blist)
# 将clist看成一个元素加到blist中
    blist.append(clist)
    print(blist)
# 更新list中的元素
def list_update():
    elist = [10,20,30,40,41,60]
    elist[4]=50
    print(elist)
# 排序list中的元素
def list_order_by():
    flist = [10,60,50,100,70,30]
    # 从小到大排序
    flist.sort()
    print(flist)
    # 从大到小排序
    flist.sort(reverse=True)
    print(flist)
#去重list中的元素
def list_distinct():
    glist = [1,1,2,2,3,5,5,4,4,6,8,6,7]
    # 使用set方法对list进行去重,去重后不是list类型,用list()方法 将这个数据转换成list数据
    glist=list(set(glist))
    print(glist)
    # 获取list长度
    print(len(glist))
    print('-------------------------------------')


if __name__ == '__main__':
    list_fangfa()
    list_del()
    list_add()
    list_update()
    list_order_by()
    list_distinct()
