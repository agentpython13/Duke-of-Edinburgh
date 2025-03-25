n  = int(input())
if n % 2 != 0:
    print(n)
else:
    while n % 2 == 0:
        n //= 2
    print(n)