process_int = int(input()) # Process의 수

arrival_time = [0 for i in range(process_int)] # 도착 시간
burst_time =[0 for i in range(process_int)] # 실행 시간

# 도착 시간, 실행 시간 입력 #
for process in range(process_int):
    arrival_time[process], burst_time[process] = map(int, input().split())

TAT = [] # Turnaround Time (동작 시간)
ATAT = 0 # Average Turnaround Time (평균 동작 시간)
WT = [0] # Waiting Time (대기 시간)
AWT = 0 # Average Waiting Time (평균 대기 시간)

# 도착 시간 정렬 #
for i in range(process_int):
    for j in range(i+1, process_int):
        if arrival_time[i] > arrival_time[j]:
            arrival_time[i], arrival_time[j] = arrival_time[j], arrival_time[i]
            burst_time[i], burst_time[j] = burst_time[j], burst_time[i]

# 연산 #
for process in range(process_int):
    now_time = sum(TAT)
    TAT.append(burst_time[process])
    if arrival_time[process] < now_time: # 기다리는 경우에만
        WT.append(now_time - arrival_time[process])

ATAT = sum(TAT) / len(TAT)
AWT = sum(WT) / len(WT)

print("Average Turnaround Time:", ATAT)
print("Average Waiting Time:", AWT)