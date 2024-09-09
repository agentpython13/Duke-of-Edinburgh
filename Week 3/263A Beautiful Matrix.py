matrix = [[int(x) for x in input().split(" ")],
          [int(x) for x in input().split(" ")],
          [int(x) for x in input().split(" ")],
          [int(x) for x in input().split(" ")],
          [int(x) for x in input().split(" ")]]


for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] == 1:
            print(abs(2-row)+abs(2-col))