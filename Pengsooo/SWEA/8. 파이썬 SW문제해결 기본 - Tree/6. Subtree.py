def Subtree(target_node):
    global cnt
    for lines in line_lst:
        if lines[0] == target_node:
            cnt += 1
            new_target_node = lines[1]
            if new_target_node == 0:
                return
            Subtree(new_target_node)


T = int(input()) # Testcase
for test_case in range(T):
    line_num, target_node = map(int, input().split())
    temp_lst = list(map(int, input().split()))
    line_lst = []
    cnt = 1
    for i in range(0, len(temp_lst), 2):
        line_lst.append([temp_lst[i], temp_lst[i+1]])
    Subtree(target_node)
    print("#{} {}".format(test_case+1, cnt))


