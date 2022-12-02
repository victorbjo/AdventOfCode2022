file = "data.txt"
data = []
with open(file, "r") as w:
    data = w.read().split("\n")
data.pop(-1)
convert = {"A":"1","B":"2","C":"3"}
win = {"A":"C", "B":"A", "C":"B"}
lose = {"A":"B", "B":"C", "C":"A"}
scoreDict = {"Z":6, "Y":3, "X":0}
score = 0
for play in data:
    if play[2] == "Z":
        score += int(convert[lose[play[0]]])
    elif play[2] == "X":
        score += int(convert[win[play[0]]])
    else:
        score += int(convert[play[0]])
    score += int(scoreDict[play[2]])
print(score)