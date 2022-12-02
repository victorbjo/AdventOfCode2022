file = "data.txt"
data = [0]
with open(file, "r") as w:
    for line in w:
        if line == "\n":
            data.append(0)
        else:
            data[-1] += int(line)
max = 0
for val in data:
    if val > max:
        max = val
print(max)