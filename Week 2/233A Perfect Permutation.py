n = int(input())
if n % 2 != 0:
    print(-1)
else:
    s = ""
    for number in range(2, n+2, 2):
        s += str(number) + ' '
        s += str(number-1) + " "
    print(s)
