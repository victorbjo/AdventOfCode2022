file = "data.txt"
data = []
with open(file, "r") as w:
    data = w.read().split("\n")
def charToNum(char):
    if char.isupper() :
        return ord(char) - 38
    return ord(char) - 96

result = 0
for string in data:
    str0 = string[:int(len(string)/2)]
    str1 = string[int(len(string)/2):]
    for char in str0:
        if char in str1:
            result+=charToNum(char)
            break
print(result)