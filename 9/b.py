file = "data.txt"
with open(file, "r") as w:
    data = w.read().split("\n")
rope=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
prevH = rope[0].copy()
visitedPlaces = []
def updateTail(rope, oldRope):
    for i in range(1, len(rope)):
        head = rope[i-1]
        tail = rope[i]
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
                if abs(oldRope[i-1][0] - head[0]) + abs(oldRope[i-1][1] - head[1]) == 2:
                    move = [head[0]-oldRope[i-1][0], head[1]-oldRope[i-1][1]]
                    tail[0] += move[0]
                    tail[1] += move[1]
                else:
                    if head[0] == oldRope[i-1][0]:
                        tail[0] = int(head[0])
                        tail[1] += head[1]-oldRope[i-1][1]
                    else:
                        tail[0] += head[0]-oldRope[i-1][0]
                        tail[1] = int(head[1])
            elif manhattan == 4:
                tail[0] += head[0]-oldRope[i-1][0]
                tail[1] += head[1]-oldRope[i-1][1]
        
                
def copyList(list):
    newList = []
    for i in range(len(list)):
        tempL = []
        for j in range(len(list[i])):
            tempL.append(list[i][j])
        newList.append(tempL)
    return newList

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

        old = copyList(rope)
        rope[0][0] += move[0]
        rope[0][1] += move[1]

        updateTail(rope, old)
        if rope[-1] not in visitedPlaces:
            visitedPlaces.append(copyList(rope)[-1])
        print(rope)
print(len(visitedPlaces))
