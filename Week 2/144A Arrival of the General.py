n = int(input())
heights = [int(x) for x in input().split()]

seconds = 0

ax = min(heights)
an = max(heights)

seconds += heights.index(an)
heights.remove(an)
heights.insert(0, an)

index = len(heights) - 1 - heights[::-1].index(ax)

seconds += ((len(heights) - 1) - index)

print(seconds)