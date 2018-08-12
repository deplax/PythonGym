LOWER_LIST = ["python", "python2", "python3"]
UPPER_LIST = []


def convert(data):
    return data.upper()


def main():
    print("=== print result ===")
    UPPER_LIST = map(convert, LOWER_LIST)
    print(LOWER_LIST)
    print(list(UPPER_LIST))
    print(UPPER_LIST)
    print(type(UPPER_LIST))


if __name__ == "__main__":
    main()
