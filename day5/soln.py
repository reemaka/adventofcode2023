import sys

def get_min_loc(seeds, lines):
    i = 3
    res = seeds.copy()
    done = [False] * len(res)
    for line in lines:
        if not line or line == "\n":
            done = [False] * len(res)
            i += 1
            continue
        if not line[0].isdigit():
            i += 1
            continue

        for j, elem in enumerate(res):
            if done[j]:
                continue
            dest_start, source_start, range_len = list(map(int, line.strip().split(' ')))
            if elem >= source_start and elem < (source_start + range_len):
                res[j] = dest_start + (elem - source_start)
                done[j] = True

    return min(res)

f = open(sys.argv[1] if len(sys.argv) > 1 else "ex.txt", "r")
lines = f.readlines()
f.close()

seeds = list(map(int, lines[0].split(':')[1].strip().split(' ')))
print(get_min_loc(seeds, lines))
