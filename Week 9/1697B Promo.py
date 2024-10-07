n, q = [int(x) for x in input().split()]
items = [int(x) for x in input().split()]

items.sort(reverse=True)

for query in range(q):
    x, y = [int(x) for x in input().split()]
    print(sum(items[x-y:x]))