n, k = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]
ok = []
for x in nums:
    if x + k <= 5:
        ok.append(x)
print(len(ok)//3)