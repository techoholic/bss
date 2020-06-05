import keyboard
import time
import os
print("Welcome to version 1.5 of the Sequencer! This script can record, playback, and most importantly, sequence keypress recordings called Python Keyboard Recordings (.pkr files).")
while True:
    print("\na. Record new PKR")
    print("b. Playback a recorded PKR")
    print("c. Sequence the PKRs (doesn't work yet!)")
    option = input("Type a, b, or c and press Enter: ")
    if (option == 'a'):
        print("\nRecording will start in 5")
        time.sleep(1)
        print("4")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("Recording session started. Press ` to stop")
        pkr = keyboard.record(until='`')
        print("\nRecording session ended. What do you want to do now?")
        working = True
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
            if (option == '`i' or option == 'i'):
                loop = input("\nDo you want to play the recording on loop? (y/n): ")
                running = True
                print("Playing the PKR in 5")
                time.sleep(1)
                print("4")
                time.sleep(1)
                print("3")
                time.sleep(1)
                print("2")
                time.sleep(1)
                print("1")
                time.sleep(1)
                print("Playing recording")
                while (running):
                    if (option == 'n'):
                        running = False
                    keyboard.play(pkr)
            elif (option == '`j' or option == 'j'):
                name = input("\nWhat do you want to name this PKR?: ")
                file = open("local/" + name + ".pkr", "w")
                pkrFileArray = []
                for entry in pkr:
                    pkrFileArray.append(str(entry))
                    pkrFileArray.append(str(getattr(entry, "time")))
                for entry in pkrFileArray:
                    file.write(entry + "\n")
                file.close()
            elif (option == '`k' or option == 'k'):
                print("\nRecording will start in 5")
                time.sleep(1)
                print("4")
                time.sleep(1)
                print("3")
                time.sleep(1)
                print("2")
                time.sleep(1)
                print("1")
                time.sleep(1)
                print("Recording session started. Press ` to stop")
                movSeq = keyboard.record(until='`')
                print("\nRecording session ended. What do you want to do now?")
    elif (option == 'b'):
        fileList = os.listdir("local/")
        i = 0
        for fileName in fileList:
            print(i, ". ", fileName, sep='')
            i = i + 1
        fto = input("Type the number of the PKR you want to play and press Enter: ") #file to open
        fileName = fileList[int(fto)]
        file = open("local/"+ fileName, 'r')
        pkrFromFile = file.readlines()
        file.close()
        pkrToPlay = []
        i = 0
        class KeyboardEvent:
            def __init__(self, time):
                self.time = time
        for entry in pkrFromFile:
            if (i%2 == 0):
                pkrToPlay.append(entry)
            else:
                setattr(pkrToPlay[i-1], "time", float(entry))
            i = i + 1
        keyboard.play(pkrToPlay)
