# coding=utf-8

global_value = "GLOBAL!"


def has_key_vs_in():
    print("=== has_key vs in ===")

    #  has_key 말고 in 쓰세요. 이게 더 직관적입니다.
    #  그리고 파이썬3에서 has_key 지원 안해요.
    dic = {"korea": 82, "japan": 81}

    # print(dic.has_key("korea"))
    print("korea" in dic)
    print("corea" in dic)


def true_false():
    print("=== boolean operation ===")

    # boolean 자료형은 operation 없이 사용하세요.
    true_value = True

    # good!
    if true_value:
        print("no operation")

    if true_value == True:
        print("== operation")

    if true_value is True:
        print("is operation")


def scope():
    print("=== scope ===")

    # local -> enclosed -> global -> built-in
    # LEGB rule
    # 위 순서대로 검색합니다.

    def out_func():
        non_local = "NONLOCAL!"

        def in_func():
            # 아래 두줄이 없으면 로컬변수로 찾고 선언되지 않았으니 애러 출력.
            global global_value
            nonlocal non_local  # nonlocal은 파이썬3 에만 있다.

            global_value += "!"
            non_local += "!"

            local_value = "LOCAL!"
            return ("%s %s %s" % (local_value, non_local, global_value))

        return in_func()

    print(out_func())


def return_function():
    print("=== first class function ===")

    # 별건 없고 그냥 함수 자체 리턴 됩니다.
    def out_func(x):
        def in_func(y):
            return x * y

        return in_func

    print(out_func(10)(5))
    func = out_func(10)
    print(func(5))


def operation_map():
    print("=== map ===")

    lower_list = ["python", "python2", "python3"]

    # 맵 연산 됩니다.
    def convert(data):
        return data.upper()

    upper_list = map(convert, lower_list)
    print(lower_list)
    print(list(upper_list))
    print(upper_list)
    print(type(upper_list))


def closure_attr():
    print("=== closure attr ===")

    # 1. global 변수를 사용하고 싶지 않을 때
    # 2. 클래스를 사용하지 않기 위해서
    # 3. 파이썬 데코레이터를 사용하기 위해
    def closure():
        x = 10
        k = 50  # 내부에서 사용하지 않으면 클로저 변수가 되지 않는다.

        def inner():
            y = 20
            return x + y

        return inner

    c = closure()
    for attr in c.__closure__:
        print(attr.cell_contents)


def argument():
    print("=== *args **kargs ===")
    args = ["red", "blue", "first", "second"]
    kwargs = {"red": "color", "blue": "color", "first": "number", "second": "number"}

    # 고정인자 가변인자 순서를 준수해야 함.
    def arg_test(name, *args, **kwargs):
        print("fixed argument : %s" % name)

        for arg in args:
            print("argument : %s" % arg)

        for keyword, arg in kwargs.items():
            print("argument keyword : %s, arg : %s" % (keyword, arg))

    arg_test("python", *args, **kwargs)
    print()

    arg_test("python", "red", "blue", "green", red="color", blue="color")


def partial_application_closure():
    print("=== partial_application_closure ===")

    def partial(func, *partial_args):
        def wrapper(*extra_args):
            args = list(partial_args)
            args.extend(extra_args)
            return func(*args)

        return wrapper

    def logging(year, month, day, title, content):
        print("%s-%s-%s %s:%s" % (year, month, day, title, content))

    logging("2017", "12", "28", "python2", "End of suppert in 2020")
    logging("2017", "12", "28", "python3", "Updating")

    f = partial(logging, "2017", "12", "28")
    f("python2", "End of support in 2020")
    f("python3", "Updating")


def partial_application_with_functools():
    print("=== partial_application_with_functools ===")

    from functools import partial

    def logging(year, month, day, title, content):
        print("%s-%s-%s %s:%s" % (year, month, day, title, content))

    f = partial(logging, "2017", "12", "28")
    f("python2", "End of support in 2020")
    f("python3", "Updating")


def main():
    has_key_vs_in()
    print()

    true_false()
    print()

    scope()
    print()

    return_function()
    print()

    operation_map()
    print()

    closure_attr()
    print()

    argument()
    print()

    partial_application_closure()
    print()

    partial_application_with_functools()
    print()


if __name__ == "__main__":
    main()
