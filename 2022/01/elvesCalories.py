with open("2022/01/input.txt", "r") as f:
    sortedElves = []
    cal = 0
    for line in f: 
        if (len(line) > 1):
            cal += int(line)
        else:
            sortedElves.append(cal)
            cal = 0
    else: 
        sortedElves.sort(reverse=True)
        print("The elf who is carrying the most have " + str(sortedElves[0]) + " Calories.")
        print("The top three of elves are carrying " + str(sortedElves[0] + sortedElves[1] + sortedElves[2]) + " in total.")