def rockPaper(a, b):
    score = 0
    if a == 'A':  # Opponent Rock
        if b == 'X':
            score += 4
        if b == 'Y':
            score += 8
        if b == 'Z':
            score += 3

    if a == 'B':  # Opponent Paper
        if b == 'X':
            score += 1
        if b == 'Y':
            score += 5
        if b == 'Z':
            score += 9

    if a == 'C':  # Opponent Scissors hehe
        if b == 'X':
            score += 7
        if b == 'Y':
            score += 2
        if b == 'Z':
            score += 6
    return score


inputFile = open("input.txt", "r").readlines()
sanitized = []
for x in inputFile:
    sanitized.append(x.rstrip('\n'))
#print(sanitized)

scoreTotal = 0
for item in sanitized:
    scoreTotal += rockPaper(item[0], item[-1])

print(scoreTotal)

def rockPaper2(a, b):
    score = 0
    if a == 'A':  # Opponent Rock
        if b == 'X': #game needs to lose > scissors, so 0 + 3
            score += 3
        if b == 'Y': #game needs to tie, > rock, so 3 + 1
            score += 4
        if b == 'Z': # game needs to win, so paper > 6 + 2
            score += 8

    if a == 'B':  # Opponent Paper
        if b == 'X': # game needs to lose  > rock, so 0 + 1
            score += 1
        if b == 'Y': # game needs to draw > paper, so 3 + 2
            score += 5
        if b == 'Z': # game needs to win > scissors, so 6 + 3
            score += 9

    if a == 'C':  # Opponent Scissors hehe
        if b == 'X': # Game needs to lose > paper, so 0 + 2
            score += 2
        if b == 'Y': # Game needs to draw > scissors, 3 + 3
            score += 6
        if b == 'Z': # Game needs to win > rock, 6 + 1
            score += 7
    return score

scoreTotal2 = 0
for item in sanitized:
    scoreTotal2 += rockPaper2(item[0], item[-1])

print(scoreTotal2)
