n = int(input())

solved = 0

for x in range(n):
    x = input()
    nums = x.split(" ")
    numss = [int(x) for x in nums]
    if sum(numss) >= 2:
        solved += 1

print(solved)
