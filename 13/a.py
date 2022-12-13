file = "data.txt"
data = []
with open(file, "r") as w:
    data = w.read().split("\n\n")
def parse(line):
    return eval(line)

def is_correct_order(l, r):
    if type(l) == int and type(r) == int:
        return l - r
    if type(l) == list and type(r) == list:
        if len(l) == 0 and len(r) == 0: return 0
        if len(l) == 0:                 return -1
        if len(r) == 0:                 return 1
        r1 = is_correct_order(l[0], r[0])
        return r1 if r1 != 0 else is_correct_order(l[1:], r[1:])
    return is_correct_order([l], r) if type(l) == int else is_correct_order(l, [r])


count = 0      
for i in range(len(data)):
    sides = data[i].split("\n")
    left = parse(sides[0])
    right = parse(sides[1])
    count += i+1 if (is_correct_order(left, right)<0) else 0
print(count)