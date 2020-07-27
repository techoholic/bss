print("\n*!~!* created by Techoholic *!~!*\n")
from keyboard import record, play, wait, is_pressed
import mouse
from time import sleep, time
from subprocess import Popen, PIPE, STDOUT
from os import path
from sys import executable
import seqExt
seqExt.dirInit()
print("Welcome to version 4.0 of the Sequencer! This script can record, playback, and most importantly, sequence recordings of key presses and mouse movements for games, repetitive tasks, and whatever else you can think of.")
while True:
    print("\na. Record new PKR (Python keypress recording)")
    print("b. Record new PMR (Python mouse recording)")
    print("c. Record new KMR (keyboard & mouse recording)")
    print("d. Playback saved recording")
    print("e. Sequence the recordings (and add waits, repeats, etc)")
    option = input("Type a, b, c, d, or e and press Enter: ")
    if (option == 'a'):
        print("\nThe script will start recording your keypresses in 5")
        seqExt.recPlayCountdown()
        print("Your keypresses are now being recorded. Press ` in any application to stop.")
        pkr = record(until='`')
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
            option = input("Type i, j, k, or l and then press Enter: ")
            if (option == 'i'):
                loop = input("\nDo you want to play the recording on loop? (y/n): ")
                running = True
                print("Playing the PKR in 5")
                seqExt.recPlayCountdown()
                print("Playing recording")
                while (running):
                    if (loop != 'y'):
                        running = False
                    play(pkr)
            elif (option == 'j'):
                fileName = input("\nWhat do you want to name this PKR?: ")
                seqExt.PKRtoFile(pkr, "local/recordings/" + fileName + ".pkr")
                print("Successfully saved recording to " + fileName + ".pkr!")
            elif (option == 'k'):
                print("\The script will start recording your kepresses at in 5")
                seqExt.recPlayCountdown()
                print("Your kepresses are now being recorded. Press ` in any application to stop.")
                pkr = record(until='`')
                print("\nRecording session ended. What do you want to do now?")
    elif (option == 'b'):
        print("\nThe script will start recording your mouse movements, scrolls, and clicks in 5")
        seqExt.recPlayCountdown()
        print("Your mouse is now being recorded. Press Middle Click in any application to stop.")
        pmr = mouse.record(button="middle")
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
            option = input("Type i, j, k, or l and the press Enter: ")
            if (option == 'i'):
                loop = input("\n Do you want to play the recording on loop? (y/n): ")
                running = True
                print("Playing the PMR in 5")
                seqExt.recPlayCountdown()
                print("Playing recording")
                while (running):
                    if (loop != 'y'):
                        running = False
                    mouse.play(pmr)
            elif (option == 'j'):
                fileName = input("\nWhat do you want to name this PMR?: ")
                seqExt.PMRtoFile(pmr, "local/recordings/" + fileName + ".pmr")
                print("Successfully saved recording to " + fileName + ".pmr!")
            elif (option == 'k'):
                print("\nThe script will start recording your mouse movements, clicks, and scrolls in 5")
                seqExt.recPlayCountdown()
                print("Your kepresses are now being recorded. Press ` in any application to stop.")
                pmr = mouse.record(button="middle")
                print("\nRecording session ended. What do you want to do now?")
    elif (option == 'c'):
        file = open("local/sync.sqs", 'w')
        file.write(str(time() + 5))
        file.close()
        bgMouseRec = Popen([executable, path.abspath("scripts/bgMouseRec.py")], stdout=PIPE, stderr=STDOUT)
        confirmation = False
        print("\nThe script will start recording your keyboard AND mouse in 5")
        sleep(1)
        for i in range(4, 0, -1):
            if confirmation == False:
                file = open("local/sync.sqs", 'r')
                lines = file.readlines()
                file.close()
                if len(lines) == 2:
                    confirmation = True
            print(i)
            sleep(1)
        if confirmation:
            print("\nYour keyboard and mouse are now being recorded. Press Tilde AND Middle Click to stop.")
            pkr = record(until='`')
            print("\nRecording session ended. What do you want to do now?")
            option = ''
            firstTime = True
            while (option != 'l'):
                if (firstTime == False and option != 'k'):
                    print("\nWhat now?")
                firstTime = False
                print("i. Playback the recording")
                print("j. Save the recording as a file to be accessed later")
                print("k. Discard the recording and start a new one (DOESN'T WORK YET)")
                print("l. Return to main menu")
                option = input("Type i, j, k, or l and then press Enter: ")
                if (option == 'i'):
                    loop = input("\nDo you want to play the recording on loop? (y/n): ")
                    running = True
                    print("Playing the KMR in 5")
                    seqExt.recPlayCountdown()
                    print("Playing recording")
                    while (running):
                        if (loop != 'y'):
                            running = False
                        play(pkr)
                        """OTHER STUFF HERE"""
                elif (option == 'j'):
                    fileName = input("\nWhat do you want to name this KMR?: ")
                    print("Saving...")
                    seqExt.PKRtoFile(pkr, "local/recordings/" + fileName + ".kmr")
                    file = open("local/sync.sqs", 'a')
                    file.write("\n" + fileName + ".kmr")
                    file.close()
                    attemptingToSave = True
                    pmrSaved = False
                    triesLeft = 5
                    while attemptingToSave:
                        file = open("local/sync.sqs", 'r')
                        lines = file.readlines()
                        file.close()
                        if len(lines) == 4:
                            pmrSaved = True
                        triesLeft = triesLeft - 1
                        if triesLeft == 0:
                            attemptingToSave = False
                        sleep(1)
                    if pmrSaved:
                        print("Successfully saved recording to " + fileName + ".kmr!")
                    else:
                        print("The keyboard recording has been saved but the mouse recording wasn't because 'bgMouse.py' isn't running. To run the script manually, go to the 'local' folder and run 'bgMouse.bat', then return to this program and try recording again.")
                elif (option == 'k'):
                    print("\nThe script will start recording your kepresses at in 5")
                    seqExt.recPlayCountdown()
                    print("Your kepresses are now being recorded. Press ` in any application to stop.")
                    pkr = record(until='`')
                    print("\nRecording session ended. What do you want to do now?")
        else:
            file = open("local/sync.sqs", 'w')
            file.write("")
            file.close()
            print("\nIt appears something is awry with the script that is supposed to run in the background to record the mouse. To run the script manually, go to the 'local' folder and run 'bgMouse.bat', then return to this program and try again.")
    elif (option == 'd'):
        fileName = seqExt.chooseFile()
        fileNameLines = fileName.split('.')
        if fileNameLines[len(fileNameLines)-1] == "pkr":
            PKRtoPlay = seqExt.PKRtoRec(fileName)
            loop = input("\nDo you want to play the recording on loop? (y/n): ")
            running = True
            print("Playing the PKR in 5")
            seqExt.recPlayCountdown()
            print("Playing recording")
            while (running):
                if (loop != 'y'):
                    running = False
                play(PKRtoPlay)
        elif fileNameLines[len(fileNameLines)-1] == "pmr":
            PMRtoPlay = seqExt.PMRtoRec(fileName)
            loop = input("\nDo you want to play the recording on loop? (y/n): ")
            running = True
            print("Playing the PMR in 5")
            seqExt.recPlayCountdown()
            print("Playing recording")
            while (running):
                if (loop != 'y'):
                    running = False
                mouse.play(PMRtoPlay)
        elif fileNameLines[len(fileNameLines)-1] == "kmr":
            print("\nConverting file to playable recording...")
            PKRtoPlay = seqExt.KMRtoRec(fileName, "pkr")
            file = open("local/sync.sqs", 'w')
            file.write(fileName)
            file.close()
            bgMousePlay = Popen([executable, path.abspath("scripts/bgMousePlay.py")], stdout=PIPE, stderr=STDOUT)
            print("Playing the KMR in about 5 seconds...")
            waitingForTime = True
            secondsToWait = 5
            while waitingForTime:
                file = open("local/sync.sqs", 'r')
                fileLines = file.readlines()
                file.close()
                if len(fileLines) == 2:
                    waitingForTime = False
                    waitingToPlay = True
                elif secondsToWait == 0:
                    waitingForTime = False
                    waitingToPlay = False
                else:
                    sleep(1)
                    secondsToWait = secondsToWait - 1
            if waitingToPlay == False:
                print("It appears that something is awry with the script that needs to run in the background for the mouse to be simulated. Poop.")
            while waitingToPlay:
                if float(fileLines[1]) <= time():
                    print("Playing the KMR")
                    play(PKRtoPlay)
                    waitingToPlay = False
    elif (option == 'e'):
        eventArray = []
        sfEventCount = 0
        eventCount = 0
        print("\nWecome to the part of sequencer.py where you actually sequence things.")
        openSavedProgram = input("First, do you want to load a saved program from a file? (type y or n): ")
        if (True): #This is to fix the indentation problems
            if (True):
                if (openSavedProgram == 'y'):
                    fileToOpen = seqExt.chooseFile("prog")
                    file = open("local/programs/" + fileToOpen, 'r')
                    fileAsArray = file.readlines()
                    file.close()
                    firstLine = True
                    for event in fileAsArray:
                        if (firstLine == True):
                            eventAsArray = event.split('=')
                            loopAmnt = eventAsArray[1]
                            firstLine = False
                        else:
                            eventAsArray = event.split('/')
                            eventArray.append(seqExt.progEvent(int(eventAsArray[0]), eventAsArray[1], eventAsArray[2], eventAsArray[3]))
                            eventCount = eventCount + 1
                    sfEventCount = eventCount
                print("\nTo make a program, all you have to do is choose PKR files to play, add waits in if you want, and set how many times you want to play the program. Then you can save and play!")
                print("Choose your first event: ")
                while (option != 'z'):
                    if (eventCount > 0):
                        print("\nYou currently have " + str(eventCount) + " events in your program:")
                        for event in eventArray:
                            print(event.explanation)
                        print("\nWhat now?")
                    print("v. Add wait event")
                    print("w. Add PKR from file")
                    print("x. Add mouse event")
                    print("y. Save/Execute this program")
                    print("z. Return to main menu (loses progress)")
                    option = input("Type v, w, x, y, or z and press Enter: ")
                    if (option == 'v'):
                        eventCount = eventCount + 1
                        secondsToWait = input("\nHow many seconds would you like the system to wait?: ")
                        eventArray.append(seqExt.progEvent(eventCount, float(secondsToWait), "", str(eventCount) + ". Wait " + secondsToWait + " seconds"))
                        print("Added wait event!")
                    elif (option == 'w'):
                        eventCount = eventCount + 1
                        chosenFile = seqExt.chooseFile()
                        playCount = input("How many times would you like to play recording? (default is 1): ")
                        if (playCount == ''):
                            playCount = 1
                        eventArray.append(seqExt.progEvent(eventCount, int(playCount), chosenFile, str(eventCount) + ". Play '" + chosenFile + "' " + str(playCount) + " time(s)"))
                        print("Added PKR event!")
                    elif (option == 'x'):
                        print("\np. Press and hold left click")
                        print("q. Left Click")
                        print("r. Release left click")
                        print("s. Move the cursor to a certain position")
                        xOption = input("Type p, r, or s and press Enter: ")
                        eventCount = eventCount + 1
                        if (xOption == 'p'):
                            eventArray.append(seqExt.progEvent(eventCount, "press", "", str(eventCount) + ". Press and hold left click"))
                        elif (xOption == 'q'):
                            eventArray.append(seqExt.progEvent(eventCount, "click", "", str(eventCount) + ". Left-Click"))
                        elif (xOption == 'r'):
                            eventArray.append(seqExt.progEvent(eventCount, "release", "", str(eventCount) + ". Release left click"))
                        elif (xOption == 's'):
                            print("\nPosition your mouse cursor where you want it to be moved and press '`' (tilde)")
                            wait('`')
                            position = str(get_position())
                            eventArray.append(seqExt.progEvent(eventCount, position, "posMove", str(eventCount) + ". Click at " + position))
                            print("Added postional cursor event at coordinates " + position)
                    elif (option == 'y'):
                        if (sfEventCount == 0):
                            nameOfProgram = input("\nWhat would you like to name this program?: ")
                            loopAmnt = input("How many times would you like to play this program? (infinite = -1): ")
                            file = open("local/programs/" + nameOfProgram + ".ksp", 'w') #keyboard sequencer program
                            file.write("loopAmnt=" + loopAmnt + "\n")
                            file.close()
                        if (eventCount != sfEventCount):
                            file = open("local/programs/" + nameOfProgram + ".ksp", "a+")
                            for event in eventArray:
                                if (event.id > sfEventCount):
                                    file.write(str(event.id) + "/" + str(event.count) + "/" + str(event.pkrFile) + "/" + event.explanation + "\n")
                                    sfEventCount = sfEventCount + 1
                            file.close()
                            print("\nSuccessfully saved your program to " + nameOfProgram + ".ksp!")
                        if (sfEventCount > 0):
                            print("\nStarting program in 5")
                            seqExt.recPlayCountdown()
                            programIsRunning = True
                            i = 0
                            while (programIsRunning):
                                i = i + 1
                                print("\nRunning the program for time " + str(i) + "/" + loopAmnt)
                                if (int(loopAmnt) == i):
                                    programIsRunning = False
                                for event in eventArray:
                                    if (event.pkrFile == "posMove"):
                                        print("Moving cursor to " + event.count)
                                        posTuple = (int((event.count).split('(')[1].split(',')[0]), int((event.count).split(' ')[1].split(')')[0]))
                                        move(posTuple[0], posTuple[1], 1)
                                    elif (event.pkrFile): #If the event is a recEvent
                                        running = True
                                        i2 = 0
                                        while (running):
                                            i2 = i2 + 1
                                            print("Playing '" + event.pkrFile + "' for time " + str(i2) + "/" + str(event.count))
                                            if (i2 == int(event.count)):
                                                running = False
                                            play(seqExt.PKRtoRec(event.pkrFile))
                                    elif (event.count == 'press'):
                                        print("Holding down left click")
                                        press(button="left")
                                    elif (event.count == 'click'):
                                        print("Left-Clicking")
                                        click()
                                    elif (event.count == 'release'):
                                        print("Releasing left click")
                                        release(button="left")
                                    else:
                                        print("Waiting for " + str(event.count) + " seconds")
                                        sleep(float(event.count))
                                if (is_pressed('`')):
                                    programIsRunning = False
