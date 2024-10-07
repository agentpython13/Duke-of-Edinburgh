t = int(input())
for testcase in range(t):
    n = int(input())
    if n % 2 != 0:
        n += 1
    if n < 6:
        n = 6
    elif n > 6 and n <= 8:
        n = 8
    elif n > 8 and n <= 10:
        n = 10
    print(n//2 * 5)
    
