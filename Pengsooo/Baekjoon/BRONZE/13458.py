N = int(input()) # 시험장 수
stu_lst = list(map(int, input().split())) # 응시자의 수
B, C = map(int, input().split()) # 총 감독관, 부 감독관이 볼 수 있는 응시자
ans = 0
for student in stu_lst:
    student = student - B
    ans += 1
    if student > 0:
        if student%C == 0:
            least = 0
        else: least = 1
        ans += (student // C) + least
print(ans)
