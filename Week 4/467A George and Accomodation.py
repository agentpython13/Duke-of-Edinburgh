n = int(input())
count = 0
for x in range(n):
    inside, able = [int(x) for x in input().split()]
    if able - inside >= 2:
        count += 1

print(count)