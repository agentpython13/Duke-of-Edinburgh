n, k = input().split(" ")
scores = input().split(" ")

winners = 0

for x in scores:
    if int(x) > 0 and int(x) >= int(scores[int(k)-1]):
        winners += 1

print(winners)