sackList = (open("input.txt", "r")).read().splitlines()


def getLike(str):
    firstHalf = str[:len(str) // 2]
    secondHalf = str[len(str) // 2:]
    match = set(firstHalf) & set(secondHalf)
    return match


def getLikeThree(array):
    # only works for arrays with 3 items
    return set(array[0]) & set(array[1]) & set(array[2])


def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def getPriority(inList):
    priCtr = 0
    for item in inList:
        for letter in item:
            if letter.islower():
                priCtr += (ord(letter) - 96)
            if letter.isupper():
                priCtr += (ord(letter) - 38)
    return priCtr


ansList = []
for item in sackList:
    ansList.append(getPriority(getLike(item)))

thirdedList = list(divide_chunks(sackList, 3))
ansListTwo = []
for item in thirdedList:
    ansListTwo.append(getLikeThree(item))
sumTot = 0
for item in ansListTwo:
    sumTot += getPriority(item)
print(ansListTwo)
print(sumTot)
# print(sum(ansList))
