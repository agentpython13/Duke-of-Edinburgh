t = int(input())
for testcase in range(t):
    n, k =[int(x) for x in input().split()]
    problems = [int(x) for x in input().split()]
    problems.sort()
    count = 1
    counts = [0]
    for x in range(len(problems)-1):
        if abs(problems[x]-problems[x+1]) <= k:
            count += 1
            counts.append(count)
        else:
            counts.append(count)
            count = 1
    if n == 1:
        print(0)
    else:
        print(n-max(counts))