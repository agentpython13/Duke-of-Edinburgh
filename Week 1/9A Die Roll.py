y, w = [int(x) for x in input().split()]
nums = (6 - (max(y,w)-1))
if nums == 1 or nums == 5:
    print(f"{nums}/6")
elif nums == 2:
    print("1/3")
elif nums == 4:
    print("2/3")
elif nums == 0:
    print("0/1")
elif nums == 3:
    print("1/2")
else:
    print("1/1")
    