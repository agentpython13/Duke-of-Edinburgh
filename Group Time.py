num = int(input())
if num % 5 == 0:
    print(f"{num//5}x5")
    exit()
elif num % 4 == 0:
    print(f"{num//4}x4")
    exit()
else:
    print(f"{num//3}x3")
    