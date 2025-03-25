j = 0 
s = 0

one = input()
two = input()

if one == two:
    j += 1
    s += 1
    j +=  int(input())
    s += int(input())
elif one[0] == "p":
    if two[0] == "s":
        s += 5
    else:
        j += 5
elif one[0] == "s":
    if two[0] == "p":
        j += 5
    else:
        s += 5
else:
    if two[0] == "p":
        s += 5
    else:
        j += 5
print(f"{j}-{s}")