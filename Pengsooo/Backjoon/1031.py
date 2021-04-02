## 입력받기 ##
a, b = map(int, input().split())
a_lst = []
b_lst = []

a_lst.append(input().split())
b_lst.append(input().split())

## 틀 만들기 ##
ans_lst = [1 for i in range(a*b)]

## 합 구하기 ##
hap = 0
hap2 = 0
k = 0
for i in range(a): #가로합
    hap = hap + ans_lst[i]
    for j in range(b): #세로합
        hap2 = hap2 + ans_lst[j * a]

        while hap != a_lst[idx]:
            while hap2 != b_lst[idx]:
                ans_lst[k] = 0
                k += a
            ans_lst[l] = 0
            l += 1
## 틀대로 출력하기 ##
for i in range(b):
    for j in range(a):
        x = i * a + j
        print(ans_lst[x], end=" ")
    print()
