warmers = 0
a = int(input())
if a >= 1:
    warmers += 1
    a -= 1
b = int(input())
if b >= 1:
    warmers += 1
    b -= 1
c = int(input())
if c >= 2:
    warmers += 1
    c -= 2
if warmers >= 2:
    print("toasty")
else:
    print("cold")
print(a+b+c)