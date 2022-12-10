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
valList=[20, 60, 100, 140, 180, 220]
sum = 0
for val in valList:
    sum += cycleValue[cycleList.index(val)]*val
print(sum)