file = "data.txt"
with open(file, "r") as w:
    data = w.read().split("\n")
h = [0, 0]
t = [0, 0]
prevH = h.copy()
visitedPlaces = []
def updateTail(tail, head):
    if tail[0] == head[0]:
        if tail[1] < head[1]-1:
            tail[1] += 1
        elif tail[1] > head[1]+1:
            tail[1] -= 1
    elif tail[1] == head[1]:
        if tail[0] < head[0]-1:
            tail[0] += 1
        elif tail[0] > head[0]+1:
            tail[0] -= 1
    else:
        manhattan = abs(tail[0] - head[0]) + abs(tail[1] - head[1])
        if manhattan == 3:
            tail[0] = prevH[0]
            tail[1] = prevH[1]

for motion in data:
    if "R" in motion:
        move = [0,1]
    elif "L" in motion:
        move = [0,-1]
    elif "U" in motion:
        move = [1,0]
    elif "D" in motion:
        move = [-1,0]
    for x in range(int(motion[2:])):
        prevH = h.copy()
        h[0] += move[0]
        h[1] += move[1]
        updateTail(t, h)
        if t not in visitedPlaces:
            visitedPlaces.append(t.copy())
print(len(visitedPlaces))