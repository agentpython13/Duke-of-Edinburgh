t = int(input())
for testcase in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr2 = [x for x in arr]
    arr2.sort()

    if arr == arr2:
        print(0)
    elif arr[0] == min(arr) or arr[len(arr)-1] == max(arr):
        print(1)
    elif arr[0] == max(arr) and arr[len(arr)-1] == min(arr):
        print(3)
    else:
        print(2)