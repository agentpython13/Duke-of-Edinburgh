n = int(input())
height = 0
needed = 1
while n - needed >= 0:
    n -= needed
    height += 1
    needed += height + 1
print(height)