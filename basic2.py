# coding=utf-8


def test_if():
    print("=== if ===")

    def check_boolean(value):
        if type(value) == bool:
            return True
        else:
            return False

    # 3항 연산자
    def check_boolean_ternary_operator(value):
        return True if type(value) == bool else False

    print(check_boolean(True))
    print(check_boolean("string"))

    print(check_boolean_ternary_operator(False))
    print(check_boolean_ternary_operator("string"))


def test_exception():
    print("=== exception ===")

    def read_file(file_name):
        try:
            f = open(file_name, "r")
        except:
            # 에러나면 여기로
            print("File open error")
        else:
            # 에러가 나지 않았을 때 실행하지만 에러 감지를 하지는 않는 곳. 에러감지를 하지 않아 성능에 이점이 있다.
            # try: 의 변수를 사용할 수 있다.
            # print(f.read())
            print("read file")
        finally:
            print("End file read")

    read_file("basic2.py")
    read_file("basic2.py???")


def test_range():
    print("=== range ===")

    import sys
    print("type : %s" % type(range(1000)))
    print("size : %d" % sys.getsizeof(range(1000)))

    # python3 에서는 xrange가 사라짐 기본 range가 제너레이터.


def test_enumerate():
    print("=== enumerate ===")
    alphabet_list = ["a", "b", "c"]

    def get_index_basic_method():
        i = 0
        for ch in alphabet_list:
            print("%d : %s" % (i, ch))
            i += 1

    def get_index_enumerate_method():
        for i, ch in enumerate(alphabet_list):
            print("%d : %s" % (i, ch))

    get_index_basic_method()
    get_index_enumerate_method()


def test_decorator():
    def deco(func):
        def wrapper():
            print("before")
            ret = func()
            print("after")
            return ret

        return wrapper

    @deco
    def base():
        print("base function")

    def base2():
        print("base function")

    base()
    print()
    deco(base2)()

    # 실행 결과는 2가지가 동일하다.
    # 데코레이터는 클래스나 함수를 인자로 받는다.


def test_decorator_clock():
    import time

    def measure_run_time(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()

            print("'%s' function running time : %s" % (func.__name__, end - start))
            return result

        return wrapper

    @measure_run_time
    def worker(delay_time):
        time.sleep(delay_time)

    worker(0.5)


def main():
    test_if()
    print()

    test_exception()
    print()

    test_range()
    print()

    test_enumerate()
    print()

    test_decorator()
    print()

    test_decorator_clock()
    print()


if __name__ == "__main__":
    main()
