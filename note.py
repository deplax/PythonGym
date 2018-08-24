def generate_multi(num):
    pass


def recursive_multi(num1, num2):
    print("%d x %d = %d" % (num1, num2, num1 * num2))
    if num2 < 9:
        recursive_multi(num1, num2 + 1)


def recursive_multi2(num1, num2):
    row = "%d x %d = %d\n" % (num1, num2, num1 * num2)
    return row + recursive_multi2(num1, num2 + 1) if num2 < 10 else ""


def main():
    recursive_multi(2, 1)
    print()

    print(recursive_multi2(2, 1))


if __name__ == "__main__":
    main()
