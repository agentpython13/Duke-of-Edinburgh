n = int(input())

given = [int(x) for x in input().split()]
result = ["" for x in given]

for x in range(n):
    result[x] = given.index(x+1) + 1


print(*result)

