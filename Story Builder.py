string = ""
for repeat in range(20):
    word = input()
    if word != "stop":
        string += word + ' '
    else:
        print(string)
        exit()