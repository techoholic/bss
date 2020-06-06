import keyboard
import time
import os
print("REMINDER: presing the tilde (`) to stop recording may type it in the input field so make sure to check for and remove it after recording!")
print("\n***** ***** ***** ***** ***** ***** ***** *****\n")
print("Welcome to version 2.1 of the Sequencer! This script can record, playback, and most importantly, sequence keypress recordings called Python Keyboard Recordings (.pkr files).")
def recPlayCountdown():
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
class seqEvent:
    def __init__(self, eventType, count, timelineText1, timelineText2, recToPlay):
        self.eventType = eventType
        self.count = count
        self.timelineText1 = timelineText1
        self.timelineText2 = timelineText2
        self.recToPlay = recToPlay
while True:
    print("\na. Record new PKR")
    print("b. Playback a recorded PKR")
    print("c. Sequence the PKRs (doesn't work yet!)")
    option = input("Type a, b, or c and press Enter: ")
    if (option == 'a'):
        print("\nRecording will start in 5")
        recPlayCountdown()
        print("Recording session started. Press ` in any application to stop")
        pkr = keyboard.record(until='`')
        print("\nRecording session ended. What do you want to do now?")
        option = ''
        firstTime = True
        while (option != 'l'):
            if (firstTime == False and option != 'k'):
                print("\nWhat now?")
            firstTime = False
            print("i. Playback the recording")
            print("j. Save the recording as a file to be accessed later")
            print("k. Discard the recording and start a new one")
            print("l. Return to main menu")
            option = input("Type i, j, k, or l and then press enter: ")
            if (option == 'i'):
                loop = input("\nDo you want to play the recording on loop? (y/n): ")
                running = True
                print("Playing the PKR in 5")
                recPlayCountdown()
                print("Playing recording")
                while (running):
                    if (loop != 'y'):
                        running = False
                    keyboard.play(pkr)
            elif (option == '`j' or option == 'j'):
                name = input("\nWhat do you want to name this PKR?: ")
                pkrFileArray = []
                for entry in pkr:
                    pkrFileArray.append(str(getattr(entry, "event_type")) + " " + str(getattr(entry, "scan_code")) + " " + str(getattr(entry, "name")) + " " + str(getattr(entry, "time")) + " " + str(getattr(entry, "device")) + " " + str(getattr(entry, "modifiers")) + " " + str(getattr(entry, "is_keypad")))
                file = open("local/" + name + ".pkr", "w")
                for entry in pkrFileArray:
                    file.write(entry + "\n")
                file.close()
            elif (option == '`k' or option == 'k'):
                print("\nRecording will start in 5")
                recPlayCountdown()
                print("Recording session started. Press ` to stop")
                movSeq = keyboard.record(until='`')
                print("\nRecording session ended. What do you want to do now?")
    elif (option == 'b'):
        fileList = os.listdir("local/")
        i = 0
        print("")
        for fileName in fileList:
            print(i, ". ", fileName, sep='')
            i = i + 1
        fto = input("Type the number of the PKR you want to play and press Enter: ") #file to open
        fileName = fileList[int(fto)]
        file = open("local/"+ fileName, 'r')
        pkrFromFile = file.readlines()
        file.close()
        pkrToPlay = []
        for entry in pkrFromFile:
            splitEntry = entry.split()
            newEntry = keyboard.KeyboardEvent(event_type=splitEntry[0], scan_code=int(splitEntry[1]))
            setattr(newEntry, "event_type", splitEntry[0])
            setattr(newEntry, "scan_code", int(splitEntry[1]))
            setattr(newEntry, "name", splitEntry[2])
            setattr(newEntry, "time", float(splitEntry[3]))
            setattr(newEntry, "device", splitEntry[4])
            setattr(newEntry, "modifiers", splitEntry[5])
            setattr(newEntry, "is_keypad", bool(splitEntry[6]))
            pkrToPlay.append(newEntry)
        loop = input("\nDo you want to play the recording on loop? (y/n): ")
        running = True
        print("Playing the PKR in 5")
        recPlayCountdown()
        print("Playing recording")
        while (running):
            if (loop != 'y'):
                running = False
            keyboard.play(pkrToPlay)
    elif (option == 'c'):
        planning = True
        eventCount = 0
        eventArray = []
        recordingArray = []
        recordings = 0
        while (option != 'z'):
            print("\nYou currently have " + str(eventCount) + " events in your program:")
            for event in eventArray:
                print(eventCount, ". ", event.eventType, event.timelineText1, event.count, event.timelineText2, sep='')
            print("\nWhat would you like to do now?")
            print("v. Load saved program from file")
            print("w. Add wait event")
            print("x. Add recorded event from file")
            print("y. Save/Execute this program in a file")
            print("z. Return to main menu (loses progress)")
            option = input("Type v, w, x, y, or z and press Enter: ")
            if (option == 'v'):
                print("\nNothing here yet :(")
            elif (option == 'w'):
                eventCount = eventCount + 1
                secondsToWait = input("\nHow many seconds would you like the system to wait?: ")
                waitEvent = seqEvent(eventType="Wait", count=float(secondsToWait), timelineText1=" for ", timelineText2=" seconds", recToPlay="")
                eventArray.append(waitEvent)
                print("Added wait event!")
            elif (option == 'x'):
                fileList = os.listdir("local/")
                i = 0
                print("")
                for fileName in fileList:
                    print(i, ". ", fileName, sep='')
                    i = i + 1
                fto = input("\nType the number of the PKR you want to add to the program and press Enter: ") #file to open
                fileName = fileList[int(fto)]
                file = open("local/"+ fileName, 'r')
                pkrFromFile = file.readlines()
                file.close()
                pkrToPlay = []
                for entry in pkrFromFile:
                    splitEntry = entry.split()
                    newEntry = keyboard.KeyboardEvent(event_type=splitEntry[0], scan_code=int(splitEntry[1]))
                    setattr(newEntry, "event_type", splitEntry[0])
                    setattr(newEntry, "scan_code", int(splitEntry[1]))
                    setattr(newEntry, "name", splitEntry[2])
                    setattr(newEntry, "time", float(splitEntry[3]))
                    setattr(newEntry, "device", splitEntry[4])
                    setattr(newEntry, "modifiers", splitEntry[5])
                    setattr(newEntry, "is_keypad", bool(splitEntry[6]))
                    pkrToPlay.append(newEntry)
                recordingArray.append(pkrToPlay)
                playCount = input("How many times would you like to play recording? (default is 1): ")
                if (playCount == ''):
                    playCount = 1
                recEvent = seqEvent(eventType="Play", timelineText1=" '"+ fileName + "' ", count=playCount, timelineText2=" time(s)", recToPlay=recordingArray[recordings])
                recordings = recordings + 1
                eventCount = eventCount + 1
                eventArray.append(recEvent)
                print("Added PKR event!")
            elif (option == 'y'):
                print("Nothing here yet :(")
