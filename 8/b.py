file = "data.txt"
with open(file, "r") as w:
    data = w.read().split("\n")
def calculateScenicScore(y, x):
    highestDown = highestLeft = highestRight = highestUp = 0
    treesDown = 0
    for i in range(y+1, len(data)):
        highestDown = int(data[i][x])
        treesDown += 1
        if int(data[y][x]) <= highestDown:
            break
    treesUp = 0
    for i in range(1, y+1):
        j = y - i
        highestUp = int(data[j][x])
        treesUp += 1
        if int(data[y][x]) <= highestUp:
            break
    treesLeft = 0
    for i in range(1, x+1):
        j = x - i
        highestLeft = int(data[y][j])
        treesLeft += 1
        if int(data[y][x]) <= highestLeft:
            break
    treesRight = 0
    for i in range(x+1, len(data[0])):
        highestRight = int(data[y][i])
        treesRight += 1
        if int(data[y][x]) <= highestRight:
            break
    return treesDown * treesUp * treesLeft * treesRight
scenicScore = 0
for idx, treeLine in enumerate(data):
    for idy, tree in enumerate(treeLine):
        scenicScore = max(calculateScenicScore(idx, idy), scenicScore)
        if calculateScenicScore(idx, idy) == 8:
            #print(idx, idy)
            pass
#print(calculateScenicScore(3,3))

print(scenicScore)