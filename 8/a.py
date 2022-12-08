file = "data.txt"
with open(file, "r") as w:
    data = w.read().split("\n")
print(data)
count = 0
visibleTrees = []
for idx, treeLine in enumerate(data):
    #print(treeLine)
    currentTreeLeft = -1
    currentTreeRight = -1
    for idx2, tree in enumerate(treeLine):
        if int(treeLine[idx2]) > currentTreeLeft:
            print(int(treeLine[idx2]), currentTreeLeft, idx)
            currentTreeLeft = int(treeLine[idx2])
            if [idx, idx2] not in visibleTrees:
                visibleTrees.append([idx, idx2])
        if int(treeLine[-(idx2+1)]) > currentTreeRight:
            currentTreeRight = int(treeLine[-(idx2+1)])
            if [idx, (len(treeLine)-1)-idx2] not in visibleTrees:
                visibleTrees.append([idx, (len(treeLine)-1)-idx2])
for x in range(len(data[0])):
    currentTreeTop = -1
    currentTreeBottom = -1
    for y in range(len(data)):
        if int(data[y][x]) > currentTreeTop:
            currentTreeTop = int(data[y][x])
            if [y, x] not in visibleTrees:
                visibleTrees.append([y, x])
        if int(data[-(y+1)][x]) > currentTreeBottom:
            currentTreeBottom = int(data[-(y+1)][x])
            if [(len(data)-1)-y, x] not in visibleTrees:
                visibleTrees.append([(len(data)-1)-y, x])
print(visibleTrees)
print(len(visibleTrees))