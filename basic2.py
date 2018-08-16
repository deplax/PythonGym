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


def main():
    test_if()
    print()


if __name__ == "__main__":
    main()
