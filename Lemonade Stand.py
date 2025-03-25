x = int(input())
y = int(input())
if x >= 20 and y >= 3:
    print("A")
elif x < 20 and y >= 3:
    print("B")
elif x >= 20 and y < 3:
    print("C")
else:
    print("D")