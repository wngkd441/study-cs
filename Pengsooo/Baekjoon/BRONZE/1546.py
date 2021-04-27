n = int(input())
lst = list(map(int,input().split()))
new_lst = [100*element/max(lst) for element in lst]
print(sum(new_lst)/len(new_lst))
