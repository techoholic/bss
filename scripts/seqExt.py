from time import sleep
from os import listdir, mkdir
from keyboard import KeyboardEvent
def dirInit():
    dirContent = listdir()
    localDirPresent = False
    for inode in dirContent:
        if (inode == "local"):
            localDirPresent = True
    if (localDirPresent == False):
        mkdir("local")
        mkdir("local/recordings")
        mkdir("local/programs")
def recPlayCountdown():
    sleep(1)
    print("4")
    sleep(1)
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)
def recToFile(rec="", filePathName=""):
    file = open(filePathName, "w")
    for event in rec:
        file.write(str(event.event_type) + " " + str(event.scan_code) + " " + str(event.name) + " " + str(event.time) + " " + str(event.device) + " " + str(event.modifiers) + " " + str(event.is_keypad) + "\n")
    file.close()
def chooseFile(folder="rec"):
    print("")
    if (folder == "rec"):
        fileList = listdir("local/recordings/")
    elif (folder == "prog"):
        fileList = listdir("local/programs/")
    i = 0
    for fileName in fileList:
        print(i, ". ", fileName, sep='')
        i = i + 1
    fto = input("Type the number of the file you want and press Enter: ") #file to open
    return fileList[int(fto)]
def fileToRec(pkrFileName=""):
    if (pkrFileName):
        fileName = pkrFileName
    else:
        fileName = chooseFile()
    file = open("local/recordings/"+ fileName, 'r')
    pkrFromFile = file.readlines()
    file.close()
    pkrToPlay = []
    for entry in pkrFromFile:
        splitEntry = entry.split()
        newEntry = KeyboardEvent(event_type=splitEntry[0], scan_code=int(splitEntry[1]))
        newEntry.name = splitEntry[2]
        newEntry.time = float(splitEntry[3])
        newEntry.device = splitEntry[4]
        newEntry.modifiers = splitEntry[5]
        newEntry.is_keypad = bool(splitEntry[6])
        pkrToPlay.append(newEntry)
    return pkrToPlay
class progEvent:
    def __init__(self, id, count, pkrFile, explanation):
        self.id = id
        self.count = count
        self.pkrFile = pkrFile
        self.explanation = explanation
