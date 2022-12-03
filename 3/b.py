file = "data.txt"
data = []
with open(file, "r") as w:
    data = w.read().split("\n")
def charToNum(char):
    if char.isupper() :
        return ord(char) - 38
    return ord(char) - 96
result = 0
for x in range(int(len(data)/3)):
    i = x*3
    line0 = data[i]
    line1 = data[i+1]
    line2 = data[i+2]
    for char in line0:
        if char in line1 and char in line2:
            result+=charToNum(char)
            break
print(result)