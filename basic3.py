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


def test_generator():
    print("=== generator ===")

    # yield 자체는 return 으로 생각하면 편하다.
    # 대신 해당 위치에서 모든상태를 가지고 정지한다.
    def gen():
        yield 1
        yield 2
        yield 3

    def normal():
        return 1
        return 2
        return 3

    print(gen())
    print(normal())

    for g in gen():
        print(g)

    # for n in normal():
    #     print(n)


def test_generator2():
    print("=== generator2 ===")

    def gen():
        value = 2

        while True:
            print(value)
            value = yield

    g = gen()
    next(g)
    # send 를 사용하면 yield 위치로 값을 전송할 수 있다.
    g.send(3)
    g.send(5)


def test_generator3():
    print("=== generator3 ===")

    def gen():
        value = 1
        while True:
            value = yield value

    g = gen()
    print(next(g))
    print(g.send(2))
    print(g.send(10))
    print(g.send(5))
    print(next(g))


def test_generator4():
    print("=== generator4 ===")

    def gen(items):
        count = 0
        # 상태값은 그대로 유지
        for item in items:
            if count == 5:
                # 제너레이터에서 return 을 받으면 StopIteration 예외가 발생하며 멈춤
                return -1
            count += 1
            yield item

    for i in gen(range(8)):
        print(i)


def test_comprehension():
    print("=== comprehension ===")
    v_list = [1, 2, 3]
    v_dict_key = ["korea", "japan", "china"]
    v_dict_value = [82, 81, 86]

    def print_list_with_comprehension():
        v_list_comprehension = [x * x for x in v_list]
        print(v_list_comprehension)

    def print_list_with_for():
        result = []
        for v in v_list:
            result.append(v * v)
        print(result)

    def print_dict_with_comprehension():
        v_dict_comprehension = {k: v for k, v in zip(v_dict_key, v_dict_value)}
        print(v_dict_comprehension)

    def print_dict_with_for():
        result = {}
        for k, v in zip(v_dict_key, v_dict_value):
            result[k] = v
        print(result)

    print_list_with_comprehension()
    print_list_with_for()
    print_dict_with_comprehension()
    print_dict_with_for()


def test_comprehension_generator():
    print("=== comprehension generator ===")
    SAMPLE_LIST = [1, 2, 3, 4, 5]

    # [], {} 말고 ()를 사용하면 제너레이터가 생성된다.
    def generate_sample_list():
        result = (x * x for x in SAMPLE_LIST)
        print(result)
        return result

    def generate_list_by_range():
        result = (i * i for i in range(1, 6))
        print(result)
        return result

    def print_generator(items):
        for item in items:
            print(item)

    print_generator(generate_sample_list())
    print_generator(generate_list_by_range())


def main():
    test_iterator()
    print()

    test_iterator2()
    print()

    test_generator()
    print()

    test_generator2()
    print()

    test_generator3()
    print()

    test_generator4()
    print()

    test_comprehension()
    print()

    test_comprehension_generator()


if __name__ == "__main__":
    main()
