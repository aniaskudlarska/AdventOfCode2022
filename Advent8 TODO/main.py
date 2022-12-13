# oh god this is garbage redo this with dicts later

inpList = (open("input.txt", "r")).read().splitlines()
tempList = []
for item in inpList:
    tempList.append(list(item))


# print(tempList)


def isTallestHoriz(list, index):
    firsthalf = []
    secondhalf = []
    treeVal = int(list[index])

    for i in range(0, index):
        firsthalf.append(list[i])
    for i in range(index, len(list)):
        secondhalf.append(list[i])

    if firsthalf == [] and secondhalf == []:
        return True
    elif firsthalf != [] and secondhalf != []:
        if int(max(firsthalf)) <= treeVal or int(max(secondhalf)) <= treeVal:
            return True
    return False


def isTallestVert(list, indexX, indexY):
    # var List must be a list of lists
    treeVal = list[indexY][indexX]
    print(treeVal)
    valueList = []
    firsthalf = []
    secondhalf = []
    for item in list:
        valueList.append(item[indexX])
    print(valueList)
    for i in range(0, indexX + 1):
        firsthalf.append(valueList[i])
    for i in range(indexX, len(valueList)):
        secondhalf.append(valueList[i])

    # print(firsthalf)
    print(secondhalf)
    if firsthalf == [] and secondhalf == []:
        return True
    elif firsthalf != [] and secondhalf != []:
        if int(max(firsthalf)) <= treeVal or int(max(secondhalf)) < treeVal:
            return True
    return False


visList = 0
for item in inpList:
    print(item)
    for char in item:
        if isTallestHoriz(item, int(item[intchar])):
            visList += 1

print(visList)
