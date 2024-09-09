x = input()
y = input()
xy = x + y
z = input()
if set(xy) != set(z):
    print("NO")
    exit()
for x in set(xy):
    if xy.count(x) != z.count(x):
        print("NO")
        exit()
print("YES")