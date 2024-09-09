string = input()
orders = input()

position = 1
current = 0

for letter in orders:
    if letter == string[current]:
        position += 1
        current += 1
print(position)