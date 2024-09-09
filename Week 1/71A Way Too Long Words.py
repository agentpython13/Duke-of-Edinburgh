n = int(input())

for x in range(n):
    x = input()
    if len(x) <= 10:
        print(x)
    else:
        print(x[0] + str(len(x)-2) + x[len(x)-1])