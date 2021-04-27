n = int(input())
for i in range(n):
    flag = 0
    hap = 0
    key = input()
    for j in list(key):
        if j == "O":
            flag += 1
            hap += flag
        else:
            flag = 0
    print(hap)
