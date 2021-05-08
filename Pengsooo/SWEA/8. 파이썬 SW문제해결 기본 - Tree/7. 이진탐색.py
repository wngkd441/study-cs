def inordervisit(t):
    global value, target_node
    if t > target_node:
        return
    left_node = t * 2
    right_node = t * 2 + 1
    inordervisit(left_node)
    node_lst[t] = value
    value += 1
    inordervisit(right_node)


T = int(input()) # Testcase
for test_case in range(T):
    target_node = int(input())
    node_lst = list(0 for i in range(target_node+1))
    value = 1
    inordervisit(1)
    print("#{} {} {}".format(test_case+1, node_lst[1], node_lst[target_node//2]))