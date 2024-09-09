n, m = [int(x) for x in input().split()]
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
index = primes.index(n)
if n == 47:
    print("NO")
else:
    if primes[index+1] != m:
        print("NO")
    else:
        print("YES")