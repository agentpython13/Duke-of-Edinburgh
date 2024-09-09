nums = [int(x) for x in input().split("+")]

nums.sort()


string = ""

for x in nums:
    string += f"{str(x)}+"
string = string[:len(string)-1]

print(string)