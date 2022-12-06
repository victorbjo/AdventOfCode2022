import time
file = "data.txt"
data = []
with open(file, "r") as w:
    data = w.read()
#O(n) solution. 0.0005 seconds for 14 unique characters
def findUnique(data, length):
    count = []
    for idx, char in enumerate(data):
        if char in count:
            count = count[count.index(char)+1:]
            count.append(char)
        else:
            count.append(char)
        if len(count) == length:
            return idx+1
then = time.time()
for i in range(1000):
    findUnique(data, 14)
print((time.time() - then)/1000)