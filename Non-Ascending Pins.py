string = input()
for num in range(1,len(string)):
    if int(string[num]) <= int(string[num-1]):
        print(string[num])