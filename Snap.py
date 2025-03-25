string = input()
snaps = 0
last = 0
for num in range(1,51):
    if string[num] == string[num-1] and last != num-1:
        snaps += 1
        last = num
    
print(snaps)