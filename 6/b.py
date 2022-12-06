import time
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
#O(n) solution. 0.0028 seconds for 14 unique characters
def test(data):
    for idx, char in enumerate(data):
        if allUnique(data[idx:idx+14]):
            return(idx+14)
            break
then = time.time()
for i in range(1000):
    test(data)
print((time.time() - then)/1000)