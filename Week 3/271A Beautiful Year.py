y = int(input())

not_found = True
while not_found:
    digits = set()
    y += 1
    for x in str(y):
        digits.add(x)
    if len(digits) == 4:
        not_found = False

print(y)