def calcMoveScore(opp, ends):
    score = 0
    if (ends == "X"):
        if (opp == "A"):
            score += 3
        if (opp == "B"):
            score += 1
        if (opp == "C"):
            score += 2
    if (ends == "Y"):
        score += 3
        if (opp == "A"):
            score += 1
        if (opp == "B"):
            score += 2
        if (opp == "C"):
            score += 3
    if (ends == "Z"):
        score += 6
        if (opp == "A"):
            score += 2
        if (opp == "B"):
            score += 3
        if (opp == "C"):
            score += 1
    return score
    

with open("2022/02/input.txt", "r") as f:
    totalScore = 0
    for line in f:
        game = line.split()
        totalScore += calcMoveScore(game[0], game[1])

print(totalScore)