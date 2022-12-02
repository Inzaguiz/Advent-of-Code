def transpose(matrix):
    output = []
    for index, row in enumerate(matrix):
        row.pop()
        if (index == 0):
            for col in row:
                output.append([col])
        else :
            for index, col in enumerate(row):
                output[index].append(col)
    return output

with open("2021/03/input.txt", "r") as f:
    binaryTable = []
    trans_binaryTable = []
    
    for line in f:
        binaryTable.append([*line])
    trans_binaryTable = transpose(binaryTable)
    
gamma = ""
epsilon = ""
for a in trans_binaryTable:
    if a.count("0") > a.count("1"):
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

print(gamma)
print(epsilon)
print(int(gamma, 2) * int(epsilon, 2))