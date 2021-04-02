# 필드 만들기 #
field_lst = []
for i in range(12):
    field_lst.append(list(input()))
filed_lst = field_lst.reverse()
sero = len(field_lst)
garo = len(field_lst[0])
print(field_lst, sero, garo)


# 터지는게 있는지 #
def finding_sero(i, j, cnt):
    key = field_lst[i][j]
    if key != "." and key == field_lst[i+1][j]:
        new_i = i + 1
        cnt += 1
        if cnt != 4: finding_sero(new_i, j, cnt)
        else:
            return cnt

def finding_garo(i, j, cnt):
    key = field_lst[i][j]
    if key != "." and key == field_lst[i+1][j]:
        new_j = j + 1
        cnt += 1
        if cnt != 4: finding_sero(i, new_j, cnt)
        else:
            return cnt

for i in range(sero):
    cnt = 0
    sur_lst = []
    for j in range(garo):
        finding_sero(i, j, cnt)
        finding_garo(i, j, cnt)
print(cnt)
