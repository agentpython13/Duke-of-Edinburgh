n = int(input())

order = [x for x in input()]

changes = 0
index = 0

for x in order:
    if index == len(order)-1:
        pass
    elif x == order[index+1]:
        changes += 1
    index += 1

print(changes)