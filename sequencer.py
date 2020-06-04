import keyboard
import time
print("Welcome to version 1.1 of the Sequencer! This script can record, playback, and most importantly, sequence\n keypress recordings (called movement sequences aka movSeqs).")
while True:
    print("\na. Record new movSeq")
    print("b. Playback a recorded movSeq")
    print("c. Sequence the sequences!")
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
        movSeq = keyboard.record(until='`')
        print("\nRecording session ended. What do you want to do now?")
        working = True
        option = ''
        firstTime = True
        while (option != 'l'):
            if (firstTime == False and option != 'k'):
                print("\nWhat now?")
            firstTime = False
            print("i. Playback your recording")
            print("j. Save the recording as a file to be accessed later")
            print("k. Discard your recording and start a new one")
            print("l. Return to main menu")
            option = input("Type i, j, k, or l and then press enter: ")
            if (option == '`i' or option == 'i'):
                loop = input("\nDo you want to play the recording on loop? (y/n): ")
                running = True
                print("Playing the movSeq in 5")
                time.sleep(1)
                print("4")
                time.sleep(1)
                print("3")
                time.sleep(1)
                print("2")
                time.sleep(1)
                print("1")
                time.sleep(1)
                print("Playing movement sequence")
                while (running):
                    if (option == 'n'):
                        running = False
                    keyboard.play(movSeq)
            elif (option == '`j' or option == 'j'):
                name = input("What do you want to name this movSeq?: ")
                file = open("local/movSeqs/" + name, "w")
                file.writelines(str(movSeq))
                file.close()
            elif (option == '`k' or option == 'k'):
                print("Recording will start in 5")
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
                print("Recording session ended. What do you want to do now?")
