file = "data.txt"
data = []
class node:
    def __init__(self, data, parent, id):
        self.data = data
        self.dirs = {}
        self.parent = parent
        self.id = id
    def __repr__(self) -> str:
        return str(self.id)
class Parser:
    def __init__(self, data):
        self.head = node(0, None, "root")
        self.currentDir = self.head
        self.data = data
    def parse(self):
        for idx, line in enumerate(self.data):
            if line[0] == "$":
                self.parseCommand(line, idx)
            else:
                self.parseFile(line)
    def parseCommand(self, line, idx):
        if line == "$ ls":
            pass
        else:
            newDir = line[5:]
            if newDir == "..":
                if self.currentDir.parent != None:
                    self.currentDir = self.currentDir.parent
            else:
                self.currentDir = self.currentDir.dirs[newDir]
                print(self.currentDir, self.currentDir.parent, str(idx+1))
    def parseFile(self, line):    
        if line[:3] == "dir":
            dir = line[4:]
            self.currentDir.dirs[dir] = (node(0, self.currentDir, dir))
        else:
            currentDir = self.currentDir
            while currentDir != None:
                currentDir.data += int(line[:line.index(" "):])
                currentDir = currentDir.parent
def breadthFirstSearch(root):
    smallestDir = root
    neededData = 30000000-(70000000-root.data)
    #print(neededData)
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        if current.data < smallestDir.data and current.data >= neededData:
            smallestDir = current
        for child in current.dirs:
            queue.append(current.dirs[child])
    return smallestDir.data
with open(file, "r") as w:
    data = w.read().split("\n")
parser = Parser(data)
parser.parse()
print (breadthFirstSearch(parser.head))
print(parser.head.data)