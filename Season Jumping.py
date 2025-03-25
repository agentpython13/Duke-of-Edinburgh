seasons = ["spring","summer","autumn","winter"]
season = input()
num = int(input())
index = seasons.index(season)
for repeat in range(num):
    if index > 3:
        index = 0
    index += 1
print(seasons[index])