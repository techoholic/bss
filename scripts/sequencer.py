print("\n*!~!* created by Techoholic *!~!*\n")
from keyboard import record, play
from mouse import press, release
from time import sleep
import seqExt
seqExt.dirInit()
print("Welcome to version 3.0 of the Sequencer! This script can record, playback, and most importantly, sequence keypress recordings called Python Keyboard Recordings (.pkr files).")
while True:
    print("\na. Record new PKR")
    print("b. Playback recorded PKR")
    print("c. Sequence the PKRs")
    option = input("Type a, b, or c and press Enter: ")
    if (option == 'a'):
        print("\nRecording will start in 5")
        seqExt.recPlayCountdown()
        print("Recording session started. Press ` in any application to stop")
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
            option = input("Type i, j, k, or l and then press enter: ")
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
                seqExt.recToFile(pkr, "../local/recordings/" + fileName + ".pkr")
                print("Successfully saved recording to " + fileName + ".pkr!")
            elif (option == 'k'):
                print("\nRecording will start in 5")
                seqExt.recPlayCountdown()
                print("Recording session started. Press ` to stop")
                pkr = record(until='`')
                print("\nRecording session ended. What do you want to do now?")
    elif (option == 'b'):
        pkrToPlay = seqExt.fileToRec()
        loop = input("\nDo you want to play the recording on loop? (y/n): ")
        running = True
        print("Playing the PKR in 5")
        seqExt.recPlayCountdown()
        print("Playing recording")
        while (running):
            if (loop != 'y'):
                running = False
            play(pkrToPlay)
    elif (option == 'c'):
        eventArray = []
        print("\nWecome to the part of sequencer.py where you actually sequence things.")
        openSavedProgram = input("First, do you want to load a saved program from a file? (type y or n): ")
        if (True): #This is to fix the indentation problems
            if (openSavedProgram == 'y'):
                sfEventCount = 1
                fileToOpen = seqExt.chooseFile("prog")
                file = open("../local/programs/" + fileToOpen, 'r')
                fileAsArray = file.readlines()
                file.close()
                counter = 0
                for event in fileAsArray:
                    if (counter == 0):
                        eventAsArray = event.split('=')
                        loopAmnt = eventAsArray[1]
                        firstLine = False
                    else:
                        eventAsArray = event.split('/')
                        eventArray.append(seqExt.progEvent(int(eventAsArray[0]), eventAsArray[1], eventAsArray[2], eventAsArray[3]))
                    counter = counter + 1
            else:
                eventCount = 0
                sfEventCount = 0
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
                        eventCount = eventCount + 1
                        pressOrRelease = input("Press (p) or release (r) left click?: ")
                        if (pressOrRelease == 'p'):
                            eventArray.append(seqExt.progEvent(eventCount, "press", "", str(eventCount) + ". Press and hold left click"))
                        elif (pressOrRelease == 'r'):
                            eventArray.append(seqExt.progEvent(eventCount, "release", "", str(eventCount) + ". Release left click"))
                    elif (option == 'y'):
                        if (sfEventCount == 0):
                            nameOfProgram = input("\nWhat would you like to name this program?: ")
                            loopAmnt = input("How many times would you like to play this program? (infinite = -1): ")
                            file = open("../local/programs/" + nameOfProgram + ".ksp", 'w') #keyboard sequencer program
                            file.write("loopAmnt=" + loopAmnt + "\n")
                            file.close()
                        if (eventCount != sfEventCount):
                            file = open("../local/programs/" + nameOfProgram + ".ksp", "a+")
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
                        if (event.pkrFile): #If the event is a recEvent
                            running = True
                            i2 = 0
                            while (running):
                                i2 = i2 + 1
                                print("Playing '" + event.pkrFile + "' for time " + str(i2) + "/" + str(event.count))
                                if (i2 == int(event.count)):
                                    running = False
                                play(seqExt.fileToRec(event.pkrFile))
                        elif (event.count == 'press'):
                            print("Holding down left click")
                            press(button="left")
                        elif (event.count == 'release'):
                            print("Releasing left click")
                            release(button="left")
                        else:
                            print("Waiting for " + str(event.count) + " seconds")
                            sleep(float(event.count))
