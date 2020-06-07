print("\n*!~!* created by Techoholic *!~!*\n")
from keyboard import record, play
import seqExt
seqExt.dirStatus()
print("Welcome to version 2.5 of the Sequencer! This script can record, playback, and most importantly, sequence keypress recordings called Python Keyboard Recordings (.pkr files).")
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
                seqExt.recToFile(pkr, "local/recordings/" + fileName + ".pkr")
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
        eventCount = 0
        saveFileEventCount = 0
        eventArray = []
        noName = True
        while (option != 'z'):
            print("\nYou currently have " + str(eventCount) + " events in your program:")
            for event in eventArray:
                print(event.explanation)
            print("\nWhat would you like to do now?")
            print("u. Load saved program from file")
            print("v. Add wait event")
            print("w. Add PKR from file")
            print("x. Add code snippet")
            print("y. Save/Execute this program")
            print("z. Return to main menu (loses progress)")
            option = input("Type u, v, w, x, y, or z and press Enter: ")
            if (option == 'u'):
                print("\nNothing here yet :(")
            elif (option == 'v'):
                eventCount = eventCount + 1
                secondsToWait = input("\nHow many seconds would you like the system to wait?: ")
                eventArray.append(seqExt.progEvent(eventCount, float(secondsToWait), None, str(eventCount) + ". Wait " + secondsToWait + " seconds"))
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
                print("Nothing here yet :(")
            elif (option == 'y'):
                if (saveFileEventCount != eventCount):
                    if (noName):
                        noName = False
                        nameOfProgram = input("\nWhat would you like to name this program?: ")
                        loopAmnt = input("How many times would you like to play this program? (infinite = -1): ")
                        file = open("local/" + nameOfProgram + ".ksp", 'w') #keyboard sequencer program
                        file.write("loopAmnt=" + loopAmnt + "\n")
                        file.close()
                    file = open("local/" + nameOfProgram + ".ksp", "a+")
                    for event in eventArray:
                        file.write(str(event.id) + "/" + str(event.count) + "/" + str(event.pkrFile) + "/" + event.explanation + "\n")
                        saveFileEventCount = saveFileEventCount + 1
                    file.close()
                    print("\nSuccessfully saved your program to " + nameOfProgram + ".ksp!")
                elif (saveFileEventCount > 0):
                    print("\nRun the program")
                else:
                    print("\nNothing to save or load.")
