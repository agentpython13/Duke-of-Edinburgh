n, k, l, c, d, p, nl, np = [int(x) for x in input().split()]
drink = (k * l)//nl
slices = (c * d)
salt = p // np
print(min(drink, slices, salt)//n)