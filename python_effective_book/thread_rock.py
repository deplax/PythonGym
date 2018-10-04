# https://github.com/kssim/python_effective_flow_control/blob/master/chapter5/thread/thread_lock.py
###################################
# File Name : thread_lock.py
###################################
# !/usr/bin/python3

import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format="(%(threadName)s) %(message)s")


def blocking_lock(lock):
    logging.debug("Start blocking lock")

    while True:
        time.sleep(1)
        lock.acquire()
        try:
            logging.debug("Grab it")
            time.sleep(0.5)
        finally:
            logging.debug("Release")
            lock.release()


def nonblocking_lock(lock):
    logging.debug("Start nonblocking lock")

    attempt, grab = 0, 0
    while grab < 3:
        time.sleep(1)
        logging.debug("Attempt")
        # acquire의 인자로 False를 넣으면 non-blocking
        success = lock.acquire(False)

        try:
            attempt += 1
            if success:
                logging.debug("Grap it")
                grab += 1
        finally:
            if success:
                logging.debug("Release")
                lock.release()

    logging.debug("Attempt : %s, grab : %s" % (attempt, grab))


def main():
    # 블로킹과 논블로킹이 하나의 서로 락을 잡으며 사용한다.
    # 블로킹은 데몬으로 되어 있고 논블로킹은 그렇지 않아 논블로킹이 끝나면 블로킹은 같이 종료된다.

    lock = threading.Lock()

    # (lock,) 튜플 표기임.
    blocking = threading.Thread(target=blocking_lock, name="blocking", args=(lock,))
    # 데몬으로 설정해서 메인스레드 끝나면 자동종료
    blocking.setDaemon(True)
    blocking.start()

    nonblocking = threading.Thread(target=nonblocking_lock, name="nonblocking", args=(lock,))
    nonblocking.start()


if __name__ == "__main__":
    main()
