total = 0
go=True
while go:
    x = int(input())
    if x == -1:
        go= False
    else:
        total += x
print((total//60)*30)