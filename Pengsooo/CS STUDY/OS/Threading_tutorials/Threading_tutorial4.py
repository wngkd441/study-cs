## Critical Section 생성 ##
## acquire() method 사용 ##
import time
import threading
account_balance = 0
account_balance_lock = threading.Lock()

def change_account_balance_sf2(delta):
    global account_balance
    # Critical Section #
    account_balance_lock.acquire() # True : lock이 잠글 해제될 때까지 block, True 반환.
    account_balance -= delta
    print("+",threading.currentThread().getName(),account_balance)
    account_balance += delta
    print("-",threading.currentThread().getName(),account_balance)
    account_balance_lock.release() # lock 해제

threads = [threading.Thread(target=change_account_balance_sf2, args=[3]) for i in range(10)]
for thread in threads:
    thread.start()
thread.join()