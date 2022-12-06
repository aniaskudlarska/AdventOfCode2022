
totalList, sortList = []
sortList = []
lineCtr = 0
with open('input.txt') as elfList:
    compiledList = elfList.readlines()
    totalCtr = 0
    while lineCtr < len(compiledList):
        if compiledList[lineCtr] != '\n':
            totalCtr += int(compiledList[lineCtr])
            lineCtr += 1
        else:
            totalList.append(totalCtr)
            totalCtr = 0
            lineCtr += 1

totalList.sort()
print(totalList)
print(max(totalList))
print(sum(totalList[-3:]))