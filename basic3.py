# coding=utf-8


def test_iterator():
    print("=== iterator ===")

    dummy_list = [1, 2, 3]
    dummy_dic = {"red": 1, "blue": 2, "green": 3}

    list_iter = iter(dummy_list)
    dic_iter = iter(dummy_dic)

    print("list type : %s" % type(dummy_list))
    print("dic type : %s" % type(dummy_dic))
    print("list iter type : %s" % type(list_iter))
    print("dic iter type : %s" % type(dic_iter))

    print("list iterator next : %s" % next(list_iter))
    print("dic iterator next : %s" % next(dic_iter))
    # print("list next : %s" % next(dummy_list))
    # print("dic next : %s" % next(dummy_dic))

    # 이터레이터가 아니기에 next를 사용할 수 없다.
    # list, string, tuple, open files, open sockes 등이 iterable 하다.


def test_iterator2():
    print("=== iterator2 ===")
    x = [1, 2, 3]
    x_iterator = iter(x)
    x_iterator2 = iter(x)

    print(next(x_iterator))
    print(next(x_iterator))
    print(next(x_iterator))
    # print(next(x_iterator))

    print()

    sentinel = object()
    print(next(x_iterator2, sentinel))
    print(next(x_iterator2, sentinel))
    print(next(x_iterator2, sentinel))
    print(next(x_iterator2, sentinel))
    # 기본값으로 exception을 막을 수 있다.


def main():
    test_iterator()
    print()

    test_iterator2()
    print()


if __name__ == "__main__":
    main()
