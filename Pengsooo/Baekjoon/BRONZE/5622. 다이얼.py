s = input()
tme = 0 # Total time

for letter in s:
    tme += ((ord(letter)+1)//3)-19  # ord('A')+1 = 66
    if letter >= 'S': # PQRS
        if (ord(letter)+1)%3 == 0: # S부터 3개 간격으로 앞으로 땡겨져야 함
            tme -= 1
        elif letter == 'Z': # WXYZ
            tme -= 1
print(tme)