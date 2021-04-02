def d():
    num_lst = list(range(1, 10001))
    new_lst = []
    for n in num_lst:
        hap = n
        for j in range(len(str(n))):
            hap += int(str(n)[j-1])
        if hap in num_lst:
            new_lst.append(hap)
    for element in new_lst:
        if element in num_lst:
            num_lst.remove(element)
    for value in num_lst:
        print(value)
    return 0
d()
