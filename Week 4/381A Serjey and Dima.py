n = int(input())
cards = [int(x) for x in input().split()]
turn = 1
serjey = 0
dima = 0
while len(cards) > 0:
    if turn == 1:
        serjey += max(cards[0], cards[len(cards)-1])
        cards.remove(max(cards[0], cards[len(cards)-1]))
        turn *= -1
    else:
        dima += max(cards[0], cards[len(cards)-1])
        cards.remove(max(cards[0], cards[len(cards)-1]))
        turn *= -1

print(str(serjey)+" "+str(dima))
        