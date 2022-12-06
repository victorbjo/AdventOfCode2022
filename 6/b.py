file = "data.txt"
data = []
with open(file, "r") as w:
    data = w.read()
def allUnique(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] == list[j]:
                return False
    return True
    return unique
for idx, char in enumerate(data):
    if allUnique(data[idx:idx+14]):
        print(idx+14)
        break
