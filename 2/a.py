file = "data.txt"
data = []
with open(file, "r") as w:
    data = w.read().split("\n")
data.pop(-1)
convert = {"X":"A","Y":"B","Z":"C"}
win = {"A":"C", "B":"A", "C":"B"}
scoreDict = {"X":1, "Y":2, "Z":3}
score = 0
for play in data:
    if play[0] == convert[play[2]]:
        score += 3
    elif win[convert[play[2]]] == play[0]:
        score += 6
    score += scoreDict[play[2]]
print(score)