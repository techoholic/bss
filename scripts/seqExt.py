from time import sleep
from os import listdir, mkdir
from keyboard import KeyboardEvent
from mouse import MoveEvent, ButtonEvent, WheelEvent
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
        file = open("local/sync", "w")
        file.close()
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
def PKRtoFile(rec="", filePathName=""):
    file = open(filePathName, 'w')
    for event in rec:
        file.write(str(event.event_type) + " " + str(event.scan_code) + " " + str(event.name) + " " + str(event.time) + " " + str(event.device) + " " + str(event.modifiers) + " " + str(event.is_keypad) + "\n")
    file.close()
def PMRtoFile(rec="", filePathName="", recType="pmr"):
    if recType == "pmr":
        file = open(filePathName, 'w')
        file.close()
    file = open(filePathName, 'a')
    for event in rec:
        if type(event) == MoveEvent:
            file.write("M " + str(event.x) + " " + str(event.y) + " " + str(event.time) + "\n")
        elif type(event) == ButtonEvent:
            file.write("B " + str(event.event_type) + " " + str(event.button) + " " + str(event.time) + "\n")
        elif type(event) == WheelEvent:
            file.write("W " + str(event.delta) + " " + str(event.time) + "\n")
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
def PKRtoRec(fileName=""):
    if fileName == "":
        fileName = chooseFile()
    file = open("local/recordings/"+ fileName, 'r')
    pkrFromFile = file.readlines()
    file.close()
    pkrToPlay = []
    for entry in pkrFromFile:
        splitEntry = entry.split()
        newEntry = KeyboardEvent(event_type=splitEntry[0], scan_code=int(splitEntry[1]))
        newEntry.name = splitEntry[2]
        try:
            newEntry.time = float(splitEntry[3])
        except:
            newEntry.name = splitEntry[2] + " " + splitEntry[3]
            newEntry.time = float(splitEntry[4])
            newEntry.device = splitEntry[5]
            newEntry.modifiers = splitEntry[6]
            newEntry.is_keypad = bool(splitEntry[7])
        else:
            newEntry.time = float(splitEntry[3])
            newEntry.device = splitEntry[4]
            newEntry.modifiers = splitEntry[5]
            newEntry.is_keypad = bool(splitEntry[6])
        pkrToPlay.append(newEntry)
    return pkrToPlay
def PMRtoRec(fileName=""):
    file = open("local/recordings/" + fileName, 'r')
    PMRfromFile = file.readlines()
    file.close()
    PMRtoPlay = []
    for entry in PMRfromFile:
        splitEntry = entry.split()
        if splitEntry[0] == 'M':
            newEntry = MoveEvent(x=int(splitEntry[1]), y=int(splitEntry[2]), time=float(splitEntry[3]))
        elif splitEntry[0] == 'B':
            newEntry = ButtonEvent(event_type=splitEntry[1], button=splitEntry[2], time=float(splitEntry[3]))
        elif splitEntry[0] == 'W':
            newEntry = WheelEvent(delta=float(splitEntry[1]), time=float(splitEntry[2]))
        PMRtoPlay.append(newEntry)
    return PMRtoPlay
def KMRtoRec(fileName="", recType=""):
    if recType == "pkr":
        file = open("local/recordings/" + fileName, 'r')
        PKRfromFile = file.readlines()
        file.close()
        PKRtoPlay = []
        readingFromFile = True
        for entry in PKRfromFile:
            if entry == "*!~!*\n":
                readingFromFile = False
            elif readingFromFile:
                splitEntry = entry.split()
                newEntry = KeyboardEvent(event_type=splitEntry[0], scan_code=int(splitEntry[1]))
                newEntry.name = splitEntry[2]
                try:
                    newEntry.time = float(splitEntry[3])
                except:
                    newEntry.name = splitEntry[2] + " " + splitEntry[3]
                    newEntry.time = float(splitEntry[4])
                    newEntry.device = splitEntry[5]
                    newEntry.modifiers = splitEntry[6]
                    newEntry.is_keypad = bool(splitEntry[7])
                else:
                    newEntry.time = float(splitEntry[3])
                    newEntry.device = splitEntry[4]
                    newEntry.modifiers = splitEntry[5]
                    newEntry.is_keypad = bool(splitEntry[6])
        return PKRtoPlay
    elif recType == "pmr":
        file = open("local/recordings/" + fileName, 'r')
        PMRfromFile = file.readlines()
        file.close()
        PMRtoPlay = []
        readingFromFile = False
        for entry in PMRfromFile:
            if entry == "*!~!*\n":
                readingFromFile = True
            elif readingFromFile and entry != "*!~!*":
                splitEntry = entry.split()
                if splitEntry[0] == 'M':
                    newEntry = MoveEvent(x=int(splitEntry[1]), y=int(splitEntry[2]), time=float(splitEntry[3]))
                elif splitEntry[0] == 'B':
                    newEntry = ButtonEvent(event_type=splitEntry[1], button=splitEntry[2], time=float(splitEntry[3]))
                elif splitEntry[0] == 'W':
                    newEntry = WheelEvent(delta=float(splitEntry[1]), time=float(splitEntry[2]))
                PMRtoPlay.append(newEntry)
        return PMRtoPlay
class progEvent:
    def __init__(self, id, count, pkrFile, explanation):
        self.id = id
        self.count = count
        self.pkrFile = pkrFile
        self.explanation = explanation
