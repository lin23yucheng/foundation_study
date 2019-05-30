
def work():
    dict_1 = {'name': 'lyc', 'age': '24'}
    print(dict_1['name'])

    dict_1.pop('age')
    print(dict_1)

    dict_2 = {'class':'1904'}
    dict_1.update(dict_2)
    print(dict_1)

    dict_1['name'] = 'lin'
    print(dict_1)

    dict_3 = {'city':'ng'}
    dict_4 = dict(dict_1,**dict_3)
    print(dict_4)

if __name__ == '__main__':
    work()


