file = "data.txt"
data = []
with open(file, "r") as w:
    data = w.read().split("\n")
containing = 0
def splitNums(pair):
    return [pair[0].split("-"), pair[1].split("-")]
for pair in data:
    assignments = pair.split(",")
    assignments = splitNums(assignments)
    if int(assignments[0][0]) <= int(assignments[1][0]) and int(assignments[0][1]) >= int(assignments[1][1]):
        containing += 1
    elif int(assignments[0][0]) >= int(assignments[1][0]) and int(assignments[0][1]) <= int(assignments[1][1]):
        containing += 1
        
print(containing)