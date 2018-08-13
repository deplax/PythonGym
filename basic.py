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
            nonlocal non_local      #nonlocal은 파이썬3 에만 있다.

            global_value += "!"
            non_local += "!"

            local_value = "LOCAL!"
            return ("%s %s %s" % (local_value, non_local, global_value))

        return in_func()

    print(out_func())


def main():
    has_key_vs_in()
    print()
    true_false()
    print()
    scope()


if __name__ == "__main__":
    main()
