
def getCalibrationVal(l):
    res = ""
    for c in l:
        try:
            n = int(c)
            res += c
        except:
            continue

    return int(res[0] + res[-1])

# PART 1
f = open("input.txt", "r")
sum = 0
for l in f:
    sum += getCalibrationVal(l)

print(sum)

# PART 2
valid = {"one": "one1one",
         "two": "two2two",
         "three": "three3three",
         "four": "four4four",
         "five": "five5five",
         "six": "six6six",
         "seven": "seven7seven",
         "eight": "eight8eight",
         "nine": "nine9nine"}

f = open("input.txt", "r")
nums = []
sum = 0
for l in f:
    line = l.strip()
    for v in valid:
        if v in line:
            line = line.replace(v, valid[v])
    sum += getCalibrationVal(line)
print(sum)
    
