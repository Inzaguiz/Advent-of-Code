maxCal = 0
cal = 0
with open("2022/01/input.txt", "r") as f:
    for line in f: 
        if (len(line) > 1):
            cal += int(line)
        else:
            maxCal = maxCal if maxCal > cal else cal
            cal = 0
    else: 
        print("The elf carrying the most calories have:", maxCal)