n = int(input())
homes = []
aways = []
for x in range(n):
    h, a = [int(x) for x in input().split()]
    homes.append(h)
    aways.append(a)
count = 0
for x in homes:
    if x in aways:
        count += aways.count(x)
print(count)