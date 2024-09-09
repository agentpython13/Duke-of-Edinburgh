string = input()
if string == "{}":
    print(0)
    exit()
string = string.replace("{", "")
string = string.replace("}", "")
string = set(string.split(", "))

print(len(string))