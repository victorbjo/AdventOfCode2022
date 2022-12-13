file = "data.txt"
data = []
with open(file, "r") as w:
    data = w.read().split("\n\n")
def parse(line):
    return eval(line)
def getFirstNum(l):
    if type(l) == int:
        return l
    if type(l) == list:
        if len(l) == 0:
            return 0
        return getFirstNum(l[0])

def orderByFirstNum(list):
    return sorted(list, key=getFirstNum)

count = 0
pairs = []      
for i in range(len(data)):
    sides = data[i].split("\n")
    pairs.append(parse(sides[0]))
    pairs.append(parse(sides[1]))
aIndex = None
bIndex = None
pairs = orderByFirstNum(pairs)
for i in range(len(pairs)):
    if getFirstNum(pairs[i]) >= 2 and aIndex == None:
        aIndex = i+1
    if getFirstNum(pairs[i]) >= 6 and bIndex == None:
        bIndex = i+2
print(aIndex*bIndex)



def isEven(num):
    if num == 0:
        return False
    if num == 1:
        return False
    if num == 2:
        return True
    if num == 3:
        num = num -2
        return isEven(num)
    if num == 4:
        num = num -2
        return isEven(num)
    ...