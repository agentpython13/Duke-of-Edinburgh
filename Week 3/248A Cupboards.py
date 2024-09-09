n = int(input())
right = []
left = []

for set in range(n):
    x, y = [int(x) for x in input().split()]
    left.append(x)
    right.append(y)

print(min(right.count(1),right.count(0))+min(left.count(1),left.count(0)))