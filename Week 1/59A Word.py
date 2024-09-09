word = input()

low = 0
upp = 0

for x in word:
    if x.isupper():
        upp += 1
    else:
        low += 1

if upp > low:
    word = word.upper()
else:
    word = word.lower()

print(word)