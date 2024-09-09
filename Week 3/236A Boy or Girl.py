string = input()

letters = set()

for x in string:
    letters.add(x)

if len(letters) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")