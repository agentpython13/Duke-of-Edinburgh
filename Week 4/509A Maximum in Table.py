n = int(input())
rows = []
rows.append([1]*n)
for repeat in range(1,n):
    row = [1]
    for x in range(1,n):
        row.insert(x,row[x-1]+rows[repeat-1][x])
    rows.append(row)
print(max(rows[n-1]))
        