n = int(input())

groups = 1

for magnet in range(n):
    if magnet == 0:
        state = input()
        x = state[1]
    else:
        state = input()
        if state[0] == x:
            groups += 1
        x = state[1]

if groups == 0:
    groups += 1

print(groups)

