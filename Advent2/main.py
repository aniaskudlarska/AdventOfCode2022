

def rockPaper(a,b):
    score = 0
    if a == 'A': #Opponent Rock
        if b == 'X':
            score += 4
        if b == 'Y':
            score += 8
        if b == 'Z':
            score += 3

    if a == 'B': #Opponent Paper
        if b == 'X':
            score += 1
        if b == 'Y':
            score += 5
        if b == 'Z':
            score += 9

    if a == 'C': #Opponent Scissors
        if b == 'X':
            score += 7
        if b == 'Y':
            score += 2
        if b == 'Z':
            score +=

