clues =[]

for clue in range(5):
    num = int(input())
    clues.append(num)
clues.sort()

print(str(clues[0]%10)+str(clues[1]%10)+str(clues[2]%10)+str(clues[3]%10)+str(clues[4]%10))
    