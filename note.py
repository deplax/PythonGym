def generate_multi(num):
    mul = ((num, x) for x in range(1, 10))
    for x, y in mul:
        print("%d x %d = %d" % (x, y, x * y))


def recursive_multi(num1, num2):
    print("%d x %d = %d" % (num1, num2, num1 * num2))
    if num2 < 9:
        recursive_multi(num1, num2 + 1)


def recursive_multi2(num1, num2):
    row = "%d x %d = %d\n" % (num1, num2, num1 * num2)
    return row + recursive_multi2(num1, num2 + 1) if num2 < 10 else ""


def odd_sum(num):
    return sum(range(1, num + 1, 2))


def odd_sum2(num):
    result = 0
    for i in range(1, int(num / 2) + 1):
        result += 2 * i - 1
    return result


def main():
    recursive_multi(2, 1)
    print()

    print(recursive_multi2(2, 1))
    print()

    generate_multi(4)
    print()

    print(odd_sum(10))
    print()

    print(odd_sum2(100))


if __name__ == "__main__":
    main()
