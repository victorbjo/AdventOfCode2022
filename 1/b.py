file = "data.txt"
data = [0]
with open(file, "r") as w:
    for line in w:
        if line == "\n":
            data.append(0)
        else:
            data[-1] += int(line)
combined = 0

for x in range(3):
    max = 0
    id = 0
    for idx, val in enumerate(data):
        if val > max:
            max = val
            id = idx
    combined += data.pop(id)
print(combined)