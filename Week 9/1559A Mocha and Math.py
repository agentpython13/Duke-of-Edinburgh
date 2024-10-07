t = int(input())
for testcase in range(t):
    n = int(input())
    ints = [int(x) for x in input().split()]
    x = ints[0]
    for num in ints:
        x = x & num
    print(x)
    
