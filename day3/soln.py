import sys

f = open(sys.argv[1] if len(sys.argv) > 1 else "input.txt", "r")

orig_lines = []
for l in f:
    orig_lines.append(l.strip())

def find_symbol_coords(ls, sym = None):
    coords = []
    for i, l in enumerate(ls):
        for j, c in enumerate(l):
            if c == '.':
                continue
            if not sym:
                if not c.isdigit():
                    coords.append((i, j))
            elif c == sym:
                coords.append((i, j))
    return coords

def get_neighbors(coord):
    x, y = coord
    return [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
            (x, y - 1), (x, y + 1),
            (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]

def extract_part_nums(coords_to_check, lines):
    part_nums = []
    for c in coords_to_check:
        x, y = c
        if x < 0 or y < 0 or x >= len(lines) or y >= len(lines[x]):
            continue
        if not lines[x][y].isdigit:
            continue

        start = y
        end = y
        while (start - 1) >= 0 and lines[x][start - 1].isdigit():
            start -= 1
        while (end + 1) < len(lines[x]) and lines[x][end + 1].isdigit():
            end += 1
        substr = lines[x][start:end+1]
        if not substr.isdigit():
            continue
        part_num = int(substr)
        part_nums.append(part_num)

        lines[x] = lines[x][:start] + ('.' * (end - start + 1)) + lines[x][end+1:]
    return part_nums

# PART 1
lines = orig_lines.copy()
coords = find_symbol_coords(lines)
ans = 0
for coord in coords:
    coords_to_check = get_neighbors(coord)
    ans += sum(extract_part_nums(coords_to_check, lines))
print(ans)

# PART 2
lines = orig_lines.copy()
coords = find_symbol_coords(lines, '*')
ans = 0
for coord in coords:
    coords_to_check = get_neighbors(coord)
    part_nums = extract_part_nums(coords_to_check, lines)
    if len(part_nums) == 2:
        ans += part_nums[0] * part_nums[1]
print(ans)