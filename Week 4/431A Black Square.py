one, two, three, four = [int(x) for x in input().split()]
string = input()
total = 0
for x in string:
    if x == "1":
        total += one
    elif x == "2":
        total += two
    elif x == "3":
        total += three
    else:
        total += four
print(total)
    