import math
n = int(input())

if n % 2 == 0:
    print(int(n/2))
else:
    print(int((math.ceil(n/2))* -1))