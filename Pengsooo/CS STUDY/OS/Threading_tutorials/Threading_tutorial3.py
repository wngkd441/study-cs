## Critical Section 생성 ##
## with 사용 ##

import threading, time

account_balance = 0
account_balance_lock = threading.Lock()  # mutual exclusion method?


def change_account_balance_sf1(delta):
    global account_balance
    # Critical Section #
    with account_balance_lock:  # 자동으로 acquire, release?
        account_balance -= delta
        print("+", threading.currentThread().getName(), account_balance)
        account_balance += delta
        print("-", threading.currentThread().getName(), account_balance)


threads = [threading.Thread(target=change_account_balance_sf1, args=[3]) for i in range(10)]
for thread in threads:
    thread.start()
thread.join()  # start에 print가 있는데 기다리는 method인 join을 뒤에 쓴다고 왜 기다려지나?? 병렬이라 그런가?