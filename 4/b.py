file = "data.txt"
data = []
with open(file, "r") as w:
    data = w.read().split("\n")
containing = 0
def splitNums(pair):
    nums0 = pair[0].split("-")
    nums1 = pair[1].split("-")
    num0 =[]
    num1 = []
    for x in range (int(nums0[0]), int(nums0[1])+1):
        num0.append(x)
    for x in range (int(nums1[0]), int(nums1[1])+1):
        num1.append(x)
    return [num0, num1]
for pair in data:
    assignments = pair.split(",")
    assignments = splitNums(assignments)
    if any(x in assignments[0] for x in assignments[1]):
        containing += 1
print(containing)  
