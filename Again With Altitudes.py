n = int(input())
ascent = 0
descent = 0
current = int(input())
for reading in range(n):
    climb = int(input())
    if climb >= current:
        ascent += (climb-current)
    else:
        descent += (current-climb)
    current = climb
print(ascent)
print(descent)
        
    