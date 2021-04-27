num_lst = []
for i in range(9):
    num_lst.append(int(input()))
print(max(num_lst), num_lst.index(max(num_lst))+1)
