nums = [int(x) for x in input().split()]

indexs = set()
for x in nums:
    indexs.add(x)

print(len(nums)-len(indexs))