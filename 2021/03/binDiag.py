with open("2021/03/input.txt", "r") as f:
    binaryTable = []
    for line in f:
        l = [*line]
        l.pop()
        binaryTable.append(l)
    
gamma = ""
epsilon = ""
for i in range(len(binaryTable[0])):
    bitAtIndex = []
    for j in binaryTable:
        bitAtIndex.append(j[i])
    if bitAtIndex.count("1") > bitAtIndex.count("0"):
        gamma += "1"
        epsilon += "0"
    else : 
        gamma += "0"
        epsilon += "1"
print(gamma)
print(epsilon)
print(int(gamma, 2) * int(epsilon, 2))