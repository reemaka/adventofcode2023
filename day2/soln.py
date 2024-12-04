import sys

f = open(sys.argv[1] if len(sys.argv) > 1 else "input.txt", "r")
lines = f.readlines()
f.close()

# Part 1
in_bag = {'red': 12, 'green': 13, 'blue': 14}
sum = 0
for l in lines:
    tokens = l.split(' ')
    game_id = int(tokens[1][:-1])
    sets = (' '.join(tokens[2:])).split(';')
    possible = True
    for s in sets:
        cubes = s.split(',')
        for c in cubes:
            count, color = c.strip().split(' ')
            if in_bag[color] < int(count):
                possible = False
                break
        if not possible:
            break
    if possible:
        sum += game_id
print(sum)

# Part 2
sum = 0
for l in lines:
    tokens = l.split(' ')
    game_id = int(tokens[1][:-1])
    sets = (' '.join(tokens[2:])).split(';')
    possible = True
    min_blue = 0
    min_red = 0
    min_green = 0
    for s in sets:
        cubes = s.split(',')
        for c in cubes:
            count, color = c.strip().split(' ')
            count = int(count)
            if color == "blue":
                min_blue = max(min_blue, count)
            elif color == "red":
                min_red = max(min_red, count)
            elif color == "green":
                min_green = max(min_green, count)
    power = min_blue * min_red * min_green
    sum += power
print(sum)