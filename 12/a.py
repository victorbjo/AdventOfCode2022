file = "data.txt"
data = []
with open(file, "r") as w:
    data = w.read().split("\n")
for idx, line in enumerate(data):
    if "S" in line:
        start = [idx, line.index("S")]
        break
nodeList = [[0 for i in range(len(data[0]))] for j in range(len(data))]
class node:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val
        self.cheapest = 100000
    def __repr__(self) -> str:
        return f"{self.val}"
    def climable(self, other):
        if ltn(self.val)-ltn(other.val) <= 1:
            return True
        return False
for idx, line in enumerate(data):
    for idx2, letter in enumerate(line):
        nodeList[idx][idx2] = node(idx, idx2, letter)
#print(nodeList)
def ltn(letter):
    if letter == "S":
        return ord("a")
    elif letter == "E":
        return ord("z")
    return ord(letter)
for idx, line in enumerate(data):
    if "S" in line:
        start = [idx, line.index("S")]
        break
queue = [nodeList[start[0]][start[1]]]
nodeList[start[0]][start[1]].cheapest = 0
while queue:
    current = queue.pop(0)
    #print(current.x, current.y)
    if current.val == "E":
        print(current.cheapest)
    if current.x > 0:
        if nodeList[current.x-1][current.y].climable(current):
            if nodeList[current.x-1][current.y].cheapest > current.cheapest+1:
                nodeList[current.x-1][current.y].cheapest = current.cheapest+1
                queue.append(nodeList[current.x-1][current.y])
    if current.x < len(data)-1:
        if nodeList[current.x+1][current.y].climable(current):
            if nodeList[current.x+1][current.y].cheapest > current.cheapest+1:
                nodeList[current.x+1][current.y].cheapest = current.cheapest+1
                queue.append(nodeList[current.x+1][current.y])
    if current.y > 0:
        if nodeList[current.x][current.y-1].climable(current):
            if nodeList[current.x][current.y-1].cheapest > current.cheapest+1:
                nodeList[current.x][current.y-1].cheapest = current.cheapest+1
                queue.append(nodeList[current.x][current.y-1])
    if current.y < len(data[0])-1:
        if nodeList[current.x][current.y+1].climable(current):
            if nodeList[current.x][current.y+1].cheapest > current.cheapest+1:
                nodeList[current.x][current.y+1].cheapest = current.cheapest+1
                queue.append(nodeList[current.x][current.y+1])