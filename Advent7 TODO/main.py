# oh god we have to do oop and parsers

class Folder:
    def __init__(self, name, contents):
        self.name = name
        self.contents = contents


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


def recurFolders(folder):
    # Return the size of a folder object and everything it contains
    fsize = 0
    for item in folder.contents:
        if isinstance(item, File):
            fsize += item.size
        elif isinstance(item, Folder):
            fsize += recurFolders(item)

    return fsize


testFold = Folder('testfold', [])
testFile = File('testfile', 300)
testFold.contents.append(testFile)

testFold2 = Folder('testfold2', [testFold])
print(testFold2.contents)
print(recurFolders(testFold2))
