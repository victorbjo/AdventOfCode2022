file = "data.txt"
data = []
with open(file, "r") as w:
    data = w.read().split("\n")

cycleList = [1]
cycleValue = [1]
for line in data:
    if line == "noop":
        cycleList.append(cycleList[-1]+1)
        cycleValue.append(cycleValue[-1])
    elif "addx" in line:
        value = line[4:]
        cycleList.append(cycleList[-1]+1)
        cycleValue.append(cycleValue[-1])
        cycleList.append(cycleList[-1]+1)
        cycleValue.append(int(cycleValue[-1]+int(value)))
        '''if cycleValue[-1] > 40:
            cycleValue[-1] = cycleValue[-1] -40'''
valList=[20, 60, 100, 140, 180, 220]
sum = 0
def makeLine(line):
        sprite = (["."]*40)
        line = line -1
        sprite[line] = "#"
        if line != 0:
            sprite[line-1] = "#"
        if line != 39:
            sprite[line+1] = "#"
        return sprite
render = [["."]*40]

for i in range(len(cycleList)):
    val = cycleValue[i]
    cyc = cycleList[i]
    val = (val+1) % 40
    line = int((i) / 40)
    if line == len(render):
        render.append(["."]*40)
    renderedLine = makeLine(val)
    pos = (i) % 40
    render[-1][pos] = renderedLine[pos]
    pass
for line in render:
    print(line, "\n")
print(cycleList)