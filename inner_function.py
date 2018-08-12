def calculator(x):
    def add(y):
        return x + y

    return add


if __name__ == "__main__":
    print(calculator(10))
    print(calculator(10)(5))
