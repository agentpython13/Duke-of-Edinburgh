n, m = [int(x) for x in input().split()]

count = 0 
a = 0

while a**2 <= n and a <= m:
    b = n - a**2
    if b**2 + a == m:
        count += 1
    a += 1
print(count)