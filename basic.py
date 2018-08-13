# coding=utf-8


def has_key_vs_in():
    #  has_key 말고 in 쓰세요. 이게 더 직관적입니다.
    #  그리고 파이썬3에서 has_key 지원 안해요.
    dic = {"korea": 82, "japan": 81}

    print("=== has_key vs in ===")
    # print(dic.has_key("korea"))
    print("korea" in dic)
    print("corea" in dic)


def true_false():
    # boolean 자료형은 operation 없이 사용하세요.
    true_value = True

    print("=== boolean operation ===")
    # good!
    if true_value:
        print("no operation")

    if true_value == True:
        print("== operation")

    if true_value is True:
        print("is operation")


def main():
    has_key_vs_in()
    print()
    true_false()


if __name__ == "__main__":
    main()
