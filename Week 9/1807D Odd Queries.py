t = int(input())
for testcase in range(t):
    n, q = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    for querie in range(q):
        l, r, k = [int(x) for x in input().split()] 
        x = sum(arr)
        x += ((r-l+1) * k) - sum(arr[l-1:r])
        
        if x % 2 != 0:
            print("YES")
        else:
            print("NO")