def solution(program, flag_rules, commands):
    answer = []
    for i in range(len(commands)): # element of commands
        flag = 1
        cnt = 0
        lst = commands[i].split()

        if program != lst[0]: # program OK?
            flag = 0
#             print('program name problem')

        for j in range(len(lst)):
            if lst[j].startswith('-') is True: # flag_name OK?
                for k in range(len(flag_rules)):
                    if lst[j] in flag_rules[k]:
                        flag_argument_type = flag_rules[k].split()[1] # flag arument_type OK?
                        if flag_argument_type == "STRING": # string?
                            if lst[j+1].isalpha() != True:
                                flag = 0
                                print('str problem')
                            if j+2 < len(lst) and lst[j+2].startswith('-') is False:
                                flag = 0
                                print('str problem')
                        elif flag_argument_type == "NUMBER": # number?
                            if lst[j+1].isdigit() == False or lst[j+2].startswith('-') is False:
                                flag = 0
                                print('num problem')
                            if j+2 < len(lst) and lst[j+2].startswith('-') is False:
                                flag = 0
                                print('num problem')
                        elif flag_argument_type == "NULL": # NULL?
                            if j+1 != len(lst):
                                flag = 0
#                                 print('null problem')
                        elif flag_argument_type == "STRINGS": # strings?
                            new_j = j
                            while lst[new_j+1].startswith('-') is False:
                                if lst[new_j+1].isalpha() != True:
                                    flag = 0
#                                     print('strs problem')
                                    break
                                new_j += 1
                                if new_j+1 == len(lst): # out of range
                                    break
                        elif flag_argument_type == "NUMBERS": # numbers?
                            new_j = j
                            while lst[new_j+1].startswith('-') is False:
                                if lst[new_j+1].isdigit() != True:
                                    flag = 0
#                                     print('nums problem')
                                    break
                                new_j += 1
                                if new_j+1 == len(lst): # out of range
                                    break
            else: # flag OK?
                cnt += 1
                if cnt == len(lst):
                    flag = 0
#                     print("flag problem")

        answer.append(flag > 0)
    return answer

solution("line", ["-s STRINGS", "-n NUMBERS", "-e NULL"], ["line -n 100 102 -s hi -e", "line -n id pwd -n 100"])
