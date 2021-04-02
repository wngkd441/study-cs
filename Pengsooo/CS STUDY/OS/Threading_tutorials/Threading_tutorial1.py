## Thread가 실행할 함수 혹은 메서드를 작성 ##

import threading  # Subthread 생성


# Subthread가 실행할 함수 혹은 메서드 #
def sum(low, high):
    total = 0
    for i in range(low, high):
        total += i
    print("Subthread", total)


t = threading.Thread(target=sum, args=(1, 100000))
# threading.Thread()함수의 target arugment에 실행할 target 함수.
# 쓰레드가 실행하는 함수의 파라미터는 args(튜플), kwargs(딕셔너리)로 지정.
t.start()

print("Main Thread")