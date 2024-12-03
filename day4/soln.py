
import sys

f = open(sys.argv[1] if len(sys.argv) > 1 else "input.txt", "r")

lines = []
for l in f:
    lines.append(l)

def get_nums(substr):
    nums = filter(lambda x: x.isdigit(), substr.strip().split(' '))
    return list(map(int, nums))

def calc_points(winning, have):
    points = 0
    for w in winning:
        if w in have:
            if points == 0:
                points = 1
            else:
                points *= 2
    return points

def calc_num_won(winning, have):
    n = 0
    for w in winning:
        if w in have:
            n += 1
    return n

def parse_winning_and_have(line):
    nums = line.strip().split(':')[1]
    winning, have = nums.strip().split('|')
    winning = get_nums(winning)
    have = get_nums(have)
    return winning, have


# PART 1
total_points = 0
for l in lines:
    winning, have = parse_winning_and_have(l)
    total_points += calc_points(winning, have)
print(total_points)

# PART 2
num_instances = [1] * len(lines)
for i, l in enumerate(lines):
    winning, have = parse_winning_and_have(l)
    num_won = calc_num_won(winning, have)

    for j in range(i + 1, i + 1 + num_won):
        # Each instance of card i wins an instance of card j
        num_instances[j] += num_instances[i]
print(sum(num_instances))
