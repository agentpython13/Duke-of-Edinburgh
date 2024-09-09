n = int(input())

fractions = [int(x) for x in input().split()]

den = len(fractions) * 100
num = sum(fractions)

print(((sum(fractions))/(len(fractions) * 100))* 100)