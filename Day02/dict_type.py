import json
# 字典以{ }包起来,:前面是key,后面是value;多个键值对用 , 分隔开
adict = {'username':'admin','password':'123456'}
# 字典是无序的,他没有索引,只能通过key去访问value,并且key不能重复
def dict_sel():
    print(adict['username'])
def dict_updat():
    adict['username'] = 'linyucheng'
    print(adict)
def dict_del():
    adict.pop('username')
    print(adict)
def dict_add():
    adict['age'] = 24
    print(adict)
    bdict = {'list':[1,2,8],'tuple':(4,9)}
    # 合并方法一:
    adict.update(bdict)
    print(adict)
    #合并方法二:
    cdict = {'yonghuming':'linyucheng','class':'1904'}
    ddict=dict(adict,**cdict)
    print(ddict)
    edict = {'pass':'no'}
    fdict=dict(ddict,**edict)
    print(fdict)
# 字典和字符串的转换
def dict_zhuanhuan():
    print(type(adict))
    str_dict = json.dumps(adict)
    print(str_dict)
    print(type(str_dict))
#字符串转换成字典
    dict_str='{"username":"锐雯","password":"123456"}'
    lll=json.loads(dict_str)
    print(type(lll))

if __name__ == '__main__':
    # dict_sel()
    # dict_updat()
    # dict_del()
    dict_add()
    # dict_zhuanhuan()