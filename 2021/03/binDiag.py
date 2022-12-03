with open("2021/03/input.txt", "r") as f:
    binaryTable = []
    for line in f:
        l = [*line]
        l.pop()
        binaryTable.append(l)
   
   
def rating(table, i, type):
    bitAtIndex = []
    output = []
    for j in table:
        bitAtIndex.append(j[i])
    
    for j in table:
        if type == "oxygen":
            if bitAtIndex.count("1") >= bitAtIndex.count("0"):
                if j[i] == "1":
                    output.append(j)
            else : 
                if j[i] == "0":
                    output.append(j)
        if type == "co2":
            if bitAtIndex.count("1") < bitAtIndex.count("0"):
                if j[i] == "1":
                    output.append(j)
            else : 
                if j[i] == "0":
                    output.append(j)
                
    if (len(output) == 1 or i == len(table[0])):
        return "".join(output[0])
    else:
        return rating(output, i + 1, type)

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
print("consumption:", int(gamma, 2) * int(epsilon, 2))

oxygen = rating(binaryTable, 0, "oxygen")
co2 = rating(binaryTable, 0, "co2")

print("life support:", int(oxygen, 2) * int(co2, 2))