num1 = input()
num2 = input()

ans = ""

index = 0
for x in num1:
    if str(num2[index]) == str(x):
        ans += "0"
    else:
        ans += "1"
    index += 1
print(ans)