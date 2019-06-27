def assert_int():
    try:
        assert 3>2
        assert 3==3
        assert 2<3
    except:
        print('断言失败')

def assert_str():
    a='可以'
    b='完全可以'
    c='不可以'
    try:
        assert b in c
        # assert '可以'== '可以'
        # assert b not in c

    except:
        print('断言炸了')

if __name__ == '__main__':
   assert_str()