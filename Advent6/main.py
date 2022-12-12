inpList = (open("input.txt", "r")).read().splitlines()[0]
print(inpList)


def checkUnique(list):
    return len(set(list)) == len(list)


def iterateAndReturn(str):
    bufferList = []
    listLength = 14
    pos = 0
    while pos < len(str):
        if bufferList != [] and checkUnique(bufferList):
            return pos

        while len(bufferList) <= listLength:
            bufferList.append(str[pos])
            pos += 1

        else:
            del (bufferList[0])

    return pos

print(checkUnique([]))
print(iterateAndReturn(inpList))
