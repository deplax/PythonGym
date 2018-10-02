###################################
# File Name : thread_rlock.py
###################################
# !/usr/bin/python3

import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format="(%(threadName)s) %(message)s")

RESOURCE = 0


def set_reverse(lock):
    # 별거 없이 공통자원을 리버스
    logging.debug("Start batch")

    with lock:
        logging.debug("Grab lock!")

        if RESOURCE == 0:
            set_one(lock, True)
        else:
            set_zero(lock, True)

    logging.debug("Reversed")


def set_zero(lock, end=False):
    # 별거 없이 공통자원을 set 0
    logging.debug("Start set zero")

    while True:
        with lock:
            global RESOURCE
            RESOURCE = 0
            logging.debug("Grab lock and set RESOURCE to %d." % RESOURCE)
            time.sleep(0.5)
        time.sleep(1)

        if end:
            break


def set_one(lock, end=False):
    # 별거 없이 공통자원을 set 1
    logging.debug("Start set one")

    while True:
        with lock:
            global RESOURCE
            RESOURCE = 1
            logging.debug("Grab lock and set RESOURCE to %d." % RESOURCE)
            time.sleep(0.5)
        time.sleep(1)

        if end:
            break


def main():
    # 메인 스레드를 제외하고 3개의 스레드가 동작
    # reverse에서 다시 락으로 들어오지 재진입 가능하기 때문에 데드락에 빠지지 않는다.

    # 단순히 lock = threading.Lock() 으로 변경하면 데드락에 걸리는 것을 볼 수 있다.
    lock = threading.RLock()

    zero = threading.Thread(target=set_zero, name="zero", args=(lock,))
    zero.setDaemon(True)
    zero.start()

    one = threading.Thread(target=set_one, name="one", args=(lock,))
    one.setDaemon(True)
    one.start()

    time.sleep(6)

    reverse = threading.Thread(target=set_reverse, name="reverse", args=(lock,))
    reverse.start()


if __name__ == "__main__":
    main()
