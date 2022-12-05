one = ["J","Z","G","V","T","D","B","N"]
two = ["F","P","W","D","M","R","S"]
three = ["Z","S","R","C","V"]
four = ["G", "H", "P", "Z", "J","T","R"]
five = ["F", "Q", "Z", "D", "N", "J", "C", "T"]
six = ["M", "F", "S", "G", "W", "P", "V", "N"]
seven = ["Q", "P", "B", "V", "C", "G"] 
eight = ["N", "P", "B", "Z"]
nine = ["J", "P", "W"]

file = "data.txt"
data = []
with open(file, "r") as w:
    data = w.read().split("\n")
stacks = {"1": one, "2": two, "3": three, "4": four, "5": five, "6": six, "7": seven, "8": eight, "9": nine}
for idx, lineTemp in enumerate(data):
    line = data[idx]
    line = line.replace("move", "")
    line = line.replace("to", ",")
    line = line.replace("from", ",")
    line = line.replace(" ", "")
    line = line.split(",")
    for x in range(int(line[0])):
        stacks[str(line[2])].insert(0, stacks[str(line[1])].pop(0))
        
print(one[0], two[0], three[0], four[0], five[0], six[0], seven[0], eight[0], nine[0])