# oy vey ill do this one later
# f it we'll brute force it
inpList = (open("input.txt", "r")).read().splitlines()
#print(inpList)
#9 lists of blocks
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []

#blocks are at inpList[1],[5],[9]....
#assemble each list
for item in inpList[:8]:
        if item[1] != ' ':
            list1.append(item[1])
        if item[5] != ' ':
            list2.append(item[5])
        if item[9] != ' ':
            list3.append(item[9])
        if item[13] != ' ':
            list4.append(item[13])
        if item[17] != ' ':
            list5.append(item[17])
        if item[21] != ' ':
            list6.append(item[21])
        if item[25] != ' ':
            list7.append(item[25])
        if item[29] != ' ':
            list8.append(item[29])
        if item[33] != ' ':
            list9.append(item[33])

print(list3)