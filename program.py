S = "id,name,age,act.,room,dep.\n1,Jack,68,T,13,8\n17,Betty,28,F,15,7" # Edit this table

print("\n\n" + S + "\n\n")

def solution(S, C):
    number = S.count("\n").conjugate()
    main_list = S.split()
    list_title = main_list[0].split(",")
    res_list = []

    i = 1
    for i in range(1, number + 1):
        string = "list_" + str(i)
        globals()[string] = main_list[i].split(",")
        res_list.append(globals()[string])
        i += 1

    try:
        I = list_title.index(C)
    except:
        return "Not valid"

    res_values = []
    for j in res_list:
        res_values.append(int(j[I]))

    res = max(res_values)
    
    return res

print(solution(S, 'age'))
