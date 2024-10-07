t = int(input())
for testcase in range(t):
    n, m, i, j = [int(x) for x in input().split()]
    
    if n == 1:
        print(f"1 1 1 {m}")
    else:
        x = f"1 1 {n} {m}"
        y = f"{n} 1 1 {m}"

        heat1 = 1
        heat2 = n * m
        heat3 = n
        heat4 = m

        antonheat = i * j
        heats = [heat1, heat2, heat3, heat4, antonheat]
        heats.sort()

        if heats[heats.index(antonheat)] == 0:
            if heats[1] == heat1 or heats[1] == heat2:
                print(y)
            else:
                print(x)
        elif heats[heats.index(antonheat)] == 4:
            if heats[3] == heat1 or heats[3] == heat2:
                print(y)
            else:
                print(x)
        else:
            optiona = abs(heats[heats.index(antonheat)]-heats[heats.index(antonheat)+1])
            optionb = abs(heats[heats.index(antonheat)]-heats[heats.index(antonheat)-1])
            if optiona >= optionb:
                if heats[heats.index(antonheat)+1] == heat1 or heats[heats.index(antonheat)+1] == heat2:
                    print(y)
                else:
                    print(x)
            else:
                if heats[heats.index(antonheat)-1] == heat1 or heats[heats.index(antonheat)-1] == heat2:
                    print(y)
                else:
                    print(x)





    
