file = "data.txt"
data = []
class Monkey:
    def __init__(self, monkeyText):
        self.startingItems = None
        self.operation = None
        self.test = None
        self.trueCase = None
        self.falseCase = None
        self.parse(monkeyText)
        self.monkeyBusiness = 0
    def parse(self, monkeyText):
        monkeyText = monkeyText.split("\n")
        monkeyText.pop(0)
        self.startingItems = self.parseLine(monkeyText[0]).split(", ")
        self.operation = self.parseLine(monkeyText[1])
        self.operation = self.operation[self.operation.index("=")+2:]
        self.test = int(self.parseLine(monkeyText[2], "by"))
        self.trueCase = int(self.parseLine(monkeyText[3], "y"))
        self.falseCase = int(self.parseLine(monkeyText[4], "y"))
    def parseLine(self, line, split = ":"):
        return line[line.index(split)+2:]
    def __str__(self):
        return f"Starting Items: {self.startingItems}\nOperation: {self.operation}\nTest: {self.test}\nTrue Case: {self.trueCase}\nFalse Case: {self.falseCase}"
    def performOperation(self, item):
        operations = self.operation.split(" ")
        for idx, operation in enumerate(operations):
            if operation == "old":
                operations[idx] = int(item)
            elif operation == "*" or operation == "+":
                operations[idx] = operation
            else:
                operations[idx] = int(operation)
        return eval("".join([str(operation) for operation in operations]))
    def run(self, monkeys):
        for idx, item in enumerate(self.startingItems):
            self.monkeyBusiness += 1
            self.startingItems[idx] = self.performOperation(item)
            self.startingItems[idx] = int(self.startingItems[idx]/3)
            if self.startingItems[idx]%self.test == 0:
                monkeys[self.trueCase].startingItems.append(self.startingItems[idx])
            else:
                monkeys[self.falseCase].startingItems.append(self.startingItems[idx])
        self.startingItems = [] 

        
def sortMonkeys(monkeys):
    monkeys.sort(key = lambda monkey: monkey.monkeyBusiness, reverse = True)
    return monkeys

with open(file, "r") as w:
    data = w.read()
monkeys = data.split("\n\n")
monkeys = [Monkey(monkey) for monkey in monkeys]
for x in range(20):
    for idx, monkey in enumerate(monkeys):
        monkey.run(monkeys)
monkeys = sortMonkeys(monkeys)
print(int(monkeys[0].monkeyBusiness)*int(monkeys[1].monkeyBusiness))