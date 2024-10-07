t = int(input())
for testcase in range(t):
    n, h, m = [int(x) for x in input().split()]
    hours = []
    mins = []
    for time in range(n):
        hour, min1 = [int(x) for x in input().split()]
        hours.append(hour)
        mins.append(min1)

    lengths = []
    for x in range(0, len(hours)):
        if hours[x] < h or hours[x] == h and mins[x] < m:
            z = (23 - h) + hours[x]
            y = (60 - m) + mins[x]
            if y > 60:
                y -= 60
                z += 1
            time = z * 60 + y
            lengths.append(time)
        else:
            y = 60 - m + mins[x]
            z = hours[x] -(h + 1)
            if y > 60:
                y -= 60
                z += 1
            time = z * 60 + y
            lengths.append(time)
    result = min(lengths)
    r = str(result//60) + " " + str(result - (result//60) * 60)
    print(r)
