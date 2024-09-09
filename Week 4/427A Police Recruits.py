n = int(input())
recruited = 0
order = [int(x) for x in input().split()]
count = 0
for x in order:
    if x > 0:
        recruited += x
    if x == -1:
        if recruited == 0:
            count += 1
        else:
            recruited -= 1
print(count)