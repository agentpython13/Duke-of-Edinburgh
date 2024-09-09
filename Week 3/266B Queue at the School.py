n, t = [int(x) for x in input().split()]
order = input()

for x in range(t):
    order = order.replace("BG", "GB")

print(order)
