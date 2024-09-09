n = int(input())
scores = [int(x) for x in input().split()]
best = scores[0]
worst = scores[0]
count = 0
for x in scores:
    if x > best:
        count += 1
        best = x
    if x < worst:
        count += 1
        worst = x
print(count)
