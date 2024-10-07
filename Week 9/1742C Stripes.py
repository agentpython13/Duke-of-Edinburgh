for i in range(int(input())):
    values=[]
    s=input()
    for k in range(8):
        st=input()
        values.append(st)
    if "RRRRRRRR" in values:
        print("R")
    else:
        j = 0
        while j < 8 :
            if values[0][j]==values[1][j] == values[2][j] == values[3][j] == values[4][j] == values[5][j] ==values[6][j] == values[7][j] == "B":
                print("B")
                break
            j += 1