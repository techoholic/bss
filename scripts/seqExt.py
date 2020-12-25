import keyboard
import mouse
import time
import os
def dirInit():
    dirContent = os.listdir()
    localDirPresent = False
    for inode in dirContent:
        if (inode == "local"):
            localDirPresent = True
    if (localDirPresent == False):
        os.mkdir("local")
        os.mkdir("local/recordings")
        os.mkdir("local/programs")
def countdown():
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
def nameFile(recType=""):
    fName = input("\nWhat do you want to name this " + recType + "?: ")
    try:
        file = open("local/recordings/" + fName + '.' + recType, 'w')
    except:
        fName = fName.replace('/', '-')
        fName = fName.replace('\\', '-')
        fName = fName.replace('?', '-')
        fName = fName.replace('%', '-')
        fName = fName.replace('*', '-')
        fName = fName.replace(':', '-')
        fName = fName.replace('|', '-')
        fName = fName.replace('"', '-')
        fName = fName.replace('<', '-')
        fName = fName.replace('>', '-')
    else:
        file.close()
    return fName
def PKRtoFile(rec="", fName=""):
    print("Saving your recording...")
    file = open("local/recordings/" + fName + ".pkr", 'w')
    for event in rec:
        if event.event_type == "down":
            event.event_type = 'D'
        elif event.event_type == "up":
            event.event_type = 'U'
        if event.device == None:
            event.device = 'n'
        if event.modifiers == None:
            event.modifiers = 'n'
        if not event.is_keypad:
            event.is_keypad = 0
        else:
            event.is_keypad = 1
        file.write(str(event.event_type) + " " + str(event.scan_code) + " " + str(event.name) + " " + str(event.time) + " " + str(event.device) + " " + str(event.modifiers) + " " + str(event.is_keypad) + "\n")
    file.close()
    print("Successfully saved recording to " + fName + ".pkr!")
def PMRtoFile(rec="", fName=""):
    file = open("local/recordings/" + fName + ".pmr", 'w')
    for event in rec:
        if type(event) == mouse.MoveEvent:
            file.write("M " + str(event.x) + " " + str(event.y) + " " + str(event.time) + "\n")
        elif type(event) == mouse.ButtonEvent:
            file.write("B " + str(event.event_type) + " " + str(event.button) + " " + str(event.time) + "\n")
        elif type(event) == mouse.WheelEvent:
            file.write("W " + str(event.delta) + " " + str(event.time) + "\n")
    file.close()
def chooseFile(folder="rec"):
    print("")
    if (folder == "rec"):
        fList = os.listdir("local/recordings/")
        fillIn = "recording you want to play"
    elif (folder == "prog"):
        fList = os.listdir("local/programs/")
        fillIn = "program you want to open"
    i = 0
    for fName in fList:
        print(str(i) +  ". " + fName)
        i = i + 1
    fileNotChosen = True
    firstTime = True
    while fileNotChosen:
        if firstTime:
            fToOpen = input("Type the number of the " + fillIn + " and press Enter: ")
            firstTime = False
        else:
            fToOpen = input("Invalid number: please enter a number between 0 and " + str(len(fList)-1) + ": ")
        try:
            int(fToOpen)
        except:
            pass
        else:
            fileNotChosen = False
            if int(fToOpen) < 0 or int(fToOpen) >= len(fList): fileNotChose = True
    return fList[int(fToOpen)]
def fileToPKR(fName=""):
    if fName == "":
        fName = chooseFile()
    file = open("local/recordings/"+ fName, 'r')
    pkrFromFile = file.readlines()
    file.close()
    pkrToPlay = []
    for entry in pkrFromFile:
        splitEntry = entry.split()
        newEntry = keyboard.KeyboardEvent(event_type=splitEntry[0], scan_code=int(splitEntry[1]))
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
        if newEntry.event_type == 'D':
            newEntry.event_type = "down"
        elif newEntry.event_type == 'U':
            newEntry.event_type = "up"
        if newEntry.device == 'n':
            newEntry.device = None
        if newEntry.modifiers == 'n':
            newEntry.modifiers = None
        pkrToPlay.append(newEntry)
    return pkrToPlay
def fileToPMR(fName=""):
    file = open("local/recordings/" + fName, 'r')
    PMRfromFile = file.readlines()
    file.close()
    PMRtoPlay = []
    for entry in PMRfromFile:
        splitEntry = entry.split()
        if splitEntry[0] == 'M':
            newEntry = mouse.MoveEvent(x=int(splitEntry[1]), y=int(splitEntry[2]), time=float(splitEntry[3]))
        elif splitEntry[0] == 'B':
            newEntry = mouse.ButtonEvent(event_type=splitEntry[1], button=splitEntry[2], time=float(splitEntry[3]))
        elif splitEntry[0] == 'W':
            newEntry = mouse.WheelEvent(delta=float(splitEntry[1]), time=float(splitEntry[2]))
        PMRtoPlay.append(newEntry)
    return PMRtoPlay
class waitEvent:
    def __init__(self, seconds):
        self.type = 'W' #waitEvent
        self.seconds = seconds
class recEvent:
    def __init__(self, name, playCount):
        self.type = 'R'
        self.name = name
        self.playCount = playCount
class mouseEvent:
    def __init__(self, meType, pos=()):
        self.type = 'M'
        self.meType = meType
        self.pos = pos
class progEvent:
    def __init__(self, id, count, pkrFile, explanation):
        self.id = id
        self.count = count
        self.pkrFile = pkrFile
        self.explanation = explanation
