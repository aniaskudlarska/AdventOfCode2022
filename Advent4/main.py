inpList = (open("input.txt", "r")).read().splitlines()

def rangeContain(r1, r2):
    # returns True if r1 is entirely in r2
    return r1[0] in r2 and r1[-1] in r2


def lineSplitter(inp):
    # returns a list of numbers from a string input like "16-33"
    line = inp.split("-")
    output = list(range(int(line[0]), int(line[1]) + 1))
    return output


def lineParserCompare(inp):
    # splits a line into two lists '8-17,16-49' > [8....17], [16...49]
    # then checks if either contains the other, returning true
    list1 = lineSplitter(inp.split(",")[0])
    list2 = lineSplitter(inp.split(",")[1])

    if rangeContain(list1,list2) or rangeContain(list2,list1):
        return True
    return False

def lineParserCompareAny(inp):
    # splits a line into two lists '8-17,16-49' > [8....17], [16...49]
    # then checks if either contains any overlap other, returning true
    list1 = lineSplitter(inp.split(",")[0])
    list2 = lineSplitter(inp.split(",")[1])

    if any(item in list1 for item in list2):
        return True
    return False




ctr = 0
for line in inpList:
    if lineParserCompareAny(line):
        ctr += 1
print(ctr)