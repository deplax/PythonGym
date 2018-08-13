# coding=utf-8
msg = "Hello"


def write():
    # 글로벌을 선언하지 않으면 지역변수로 받아들임.
    global msg
    msg += " World"
    print(msg)

def non_local(name):
    local_msg = "message"

    def add_name():
        nonlocal local_msg
        return local_msg + " " +  name

    print(add_name())

def main():
    print("=== print msg ===")
    print(msg)

    print("=== write function ===")
    write()

    print("=== non_local function ===")
    non_local("test")

    print("=== print msg ===")
    print(msg)


if __name__ == "__main__":
    main()
