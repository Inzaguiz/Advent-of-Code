with open("2021/02/input.txt", "r") as f:
    listMovement = []
    
    horizontalPosition = 0
    verticalPosition = 0
    aim = 0
    
    for line in f:
        listMovement.append(line.split())
    for movement in listMovement:
        match movement[0]:
            case "up":
                aim -= int(movement[1])
            case "down":
                aim += int(movement[1])
            case "forward":
                horizontalPosition += int(movement[1])
                verticalPosition += int(movement[1]) * aim
            
print(verticalPosition * horizontalPosition)