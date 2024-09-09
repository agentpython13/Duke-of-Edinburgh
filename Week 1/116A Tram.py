n = int(input())

counts = []
count = 0
for stop in range(n):
    exit, enter = [int(x) for x in input().split()]
    count -= exit
    count += enter
    counts.append(count)

print(max(counts))