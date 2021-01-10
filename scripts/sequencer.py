print("\n*!~!* created by Techoholic *!~!*\n")
import seqExt
import keyboard
import mouse
import time
seqExt.dirInit()
print("Welcome to version 5.0 of the Sequencer! This script can record, playback, and most importantly, sequence recordings of key presses and mouse movements for games, repetitive tasks, and whatever else you can think of.")
option = ''
while option != 'f':
    print("\na. Record new PKR (Python keypress recording)")
    print("b. Record new PMR (Python mouse recording)")
    print("d. Playback saved recording")
    print("e. Sequence the recordings (and add waits, repeats, etc)")
    print("f. Exit the program")
    option = input("Type a, b, d, e, or f and press Enter: ")
    if option == 'a':
        print("\nThe script will start recording your keypresses in 5")
        seqExt.countdown()
        print("Your keypresses are now being recorded. Press ` (backtick) in any application to stop.")
        pkr = keyboard.record(until="`")
        print("\nRecording session ended. What do you want to do now?")
        option = ''
        firstTime = True
        while option != 'l':
            if not firstTime and option != 'k':
                print("\nWhat now?")
            firstTime = False
            print("i. Playback the recording")
            print("j. Save the recording as a file to be played back later")
            print("k. Record another PKR (discards old one if not saved)")
            print("l. Return to main menu")
            option = input("Type i, j, k, or l and then press Enter: ")
            if option == 'i':
                loopCnt = input("\nDo you want to play the PKR a certain number of times? (-1 is infinity; just press Enter for once): ")
                running = True
                print("Playing the PKR in 5")
                seqExt.countdown()
                if not loopCnt:
                    print("Playing recording once")
                    loopCnt = 1
                else:
                    loopCnt = int(loopCnt)
                cycle = 1
                timesToRun = "infinity" if loopCnt < 0 else loopCnt
                while running:
                    if loopCnt != 1: print("Playing recording for time " + str(cycle) + '/' + str(timesToRun))
                    keyboard.play(pkr)
                    if cycle == timesToRun: running = False
                    cycle+=1
            elif option == 'j':
                fName = seqExt.nameFile(recType="pkr")
                seqExt.PKRtoFile(pkr, fName)
            elif option == 'k':
                print("\nThe script will start recording your keypresses in 5")
                seqExt.countdown()
                print("Your keypresses are now being recorded. Press ` (backtick) in any application to stop.")
                pkr = keyboard.record(until="`")
                print("\nRecording session ended. What do you want to do now?")
                option = ''
                firstTime = True
    elif option == 'b':
        print("\nThe script will start recordings your mouse movements, clicks, and scrolls in 5")
        seqExt.countdown()
        print("Your mouse is now being recorded. Press Middle Click in any application to stop.")
        pmr = mouse.record(button="middle")
        print("\nRecording session ended. What do you want to do now?")
        option = ''
        firstTime = True
        while option != 'l':
            if not firstTime and option != 'k':
                print("\nWhat now?")
            firstTime = False
            print("i. Playback the recording")
            print("j. Save the recording as a file to be played back later")
            print("k. Record another PMR (discards old one if not saved)")
            print("l. Return to main menu")
            option = input("Type i, j, k, or l and then press Enter: ")
            if option == 'i':
                loopCnt = input("\nDo you want to play the PMR a certain number of times? (-1 is infinity; just press Enter for once): ")
                running = True
                print("Playing the PMR in 5")
                seqExt.countdown()
                if not loopCnt:
                    print("Playing recording once")
                    loopCnt = 1
                else:
                    loopCnt = int(loopCnt)
                cycle = 1
                timesToRun = "infinity" if loopCnt < 0 else loopCnt
                while running:
                    if loopCnt != 1: print("Playing recording for time " + str(cycle) + '/' + str(timesToRun))
                    mouse.play(pmr)
                    if cycle == timesToRun: running = False
                    cycle+=1
            elif option == 'j':
                fName = seqExt.nameFile(recType="pmr")
                seqExt.PMRtoFile(pmr, fName)
            elif option == 'k':
                print("\nThe script will start recording your mouse movements, clicks, and scrolls in 5")
                seqExt.countdown()
                print("Your mouse is now being recorded. Press Middle Click in any application to stop.")
                pmr = mouse.record(button="middle")
                print("\nRecording session ended. What do you want to do now?")
                option = ''
                firstTime = True
    elif option == 'c':
        print("\nOh hey there! You must be curious why there is no 'c' option in this script. Well, option c is supposed to record a new KMR (keyboard & mouse recording) but I have halted development on this (and completely removed it from the script) because no one is using it and it's quite frustrating to implement for a beginner dev like me. If you really want to record and playback KMRS, use version 4.1 on GitHub and if you're interested about further development, check out the 'kmr' branch. Now on with the show!")
    elif option == 'd':
        fName = seqExt.chooseFile(folder="rec")
        print("\nConverting file to playable recording...")
        recType = ''
        if fName.split('.')[-1] == "pkr":
            pkr = seqExt.fileToPKR(fName)
            recType = "PKR"
        elif fName.split('.')[-1] == "pmr":
            pmr = seqExt.fileToPMR(fName)
            recType = "PMR"
        elif fName.split('.')[-1] == "kmr":
            print("I'm not sure how you even got a KMR file but they are not supported with this version of the program. Use version 4.1 on GitHub.")
        else:
            print("Could not open chosen file because it is not a PKR or PMR :/")
        if recType:
            loopCnt = input("\nDo you want to play the " + recType + " a certain number of times? (-1 is infinity; just press Enter for once): ")
            running = True
            print("Playing the " + recType + " in 5")
            seqExt.countdown()
            if not loopCnt:
                print("Playing recording once")
                loopCnt = 1
            else:
                loopCnt = int(loopCnt)
            cycle = 1
            timesToRun = "infinity" if loopCnt < 0 else loopCnt
            while running:
                if loopCnt != 1: print("Playing recording for time " + str(cycle) + '/' + str(timesToRun))
                if recType == "PKR":
                    keyboard.play(pkr)
                elif recType == "PMR":
                    mouse.play(pmr)
                if cycle == timesToRun: running = False
                cycle+=1
    elif option == 'e':
        events = []
        sfEventCount = 0
        print("\nWecome to the part of sequencer.py where you actually sequence things.")
        openSavedProgram = input("First, do you want to load a saved program from a file? (type y or n): ")
        if openSavedProgram  == 'y':
            print("Loading program...")
            fName = seqExt.chooseFile("prog")
            file = open("local/programs/" + fName, 'r')
            fileAsArray = file.readlines()
            file.close()
            firstLine = True
            for line in fileAsArray:
                if firstLine:
                    loopAmnt = line.split('=')[1]
                    firstLine = False
                else:
                    line = line.split('/')
                    if line[0] == 'W':
                        events.append(seqExt.waitEvent(float(line[1])))
                    elif line[0] == 'R':
                        events.append(seqExt.recEvent(line[1], int(float(line[2]))))
                    elif line[0] == 'M':
                        posAsTuple = ()
                        if line[2] != "()\n": posAsTuple = (int(line[2].split('(')[1].split(',')[0]), int(line[2].split(',')[1].split(')')[0]))
                        events.append(seqExt.mouseEvent(line[1], posAsTuple))
            sfEventCount = len(events)
        else:
            print("Making a program with seq.py is easy: just add recordings (PKRs & PMRs), mouse events, and waits to execute them in a sequence. This simple concept allows you to do pretty complex things, however. Have fun building amazing programs!\nChoose your first event:")
        while option != 'z':
            if events:
                print("\nYou currently have " + str(len(events)) + " events in your program:")
                i = 1
                for event in events:
                    if event.type == 'W':
                        print(str(i) + ". Wait for " + str(event.seconds) + " seconds")
                    elif event.type == 'R':
                        s = 's' if event.playCount != 1 else ''
                        print(str(i) + ". Play " + event.name + ' ' + str(event.playCount) + " time" + s)
                    elif event.type == 'M':
                        if event.meType == "press":
                            print(str(i) + ". Press and hold left-click")
                        elif event.meType == "release":
                            print(str(i) + ". Release left-click")
                        elif event.meType == "click":
                            print(str(i) + ". Perform a left click")
                        elif event.meType == "move":
                            print(str(i) + ". Move the mouse arrow to " + str(event.pos))
                    i+=1
                print("\nWhat now?")
            print("v. Add wait event")
            print("w. Add PKR from file")
            print("x. Add mouse event")
            print("y. Save/Execute this program")
            print("z. Return to main menu (loses progress)")
            option = input("Type v, w, x, y, or z and press Enter: ")
            if option == 'v':
                secondsToWait = input("\nHow many seconds would you like the system to wait?: ")
                events.append(seqExt.waitEvent(float(secondsToWait)))
                print("Added wait event!")
            elif option == 'w':
                chosenFile = seqExt.chooseFile()
                playCount = input("How many times would to like to play recording? (default is 1): ")
                if not playCount: playCount = 1
                events.append(seqExt.recEvent(chosenFile, float(playCount)))
                print("Added recording event!")
            elif option == 'x':
                print("\nWhat type of mouse event would you like to add?: ")
                print("p. Press and hold left-click")
                print("q. Left Click")
                print("r. Release left-click")
                print("s. Move the cursor to a certain position")
                xOption = input("Type p, r, or s and press Enter: ")
                if xOption == 'p':
                    events.append(seqExt.mouseEvent("press"))
                elif xOption == 'q':
                    events.append(seqExt.mouseEvent("click"))
                elif xOption == 'r':
                    events.append(seqExt.mouseEvent("release"))
                elif xOption == 's':
                    print("\nPosition your mouse cursor where you want it to be moved and press '`' (backtick)")
                    keyboard.wait('`')
                    position = str(mouse.get_position())
                    events.append(seqExt.mouseEvent("move", position))
                print("Added mouse event!")
            elif option == 'y':
                if not sfEventCount:
                    nameOfProgram = input("\nWhat would you like to name this program?: ")
                    loopAmnt = input("How many times would you like to play this program? (infinite = -1): ")
                    loopAmnt = 1 if not loopAmnt else int(loopAmnt)
                if len(events) > sfEventCount:
                    file = open("local/programs/" + nameOfProgram + ".ksp", "w")
                    file.write("loopAmnt=" + str(loopAmnt) + "\n")
                    sfEventCount = 0
                    for event in events:
                        file.write(event.type + '/')
                        if event.type == 'W':
                            file.write(str(event.seconds))
                        elif event.type == 'R':
                            file.write(event.name + '/' + str(event.playCount))
                        elif event.type == 'M':
                            file.write(event.meType + '/' + str(event.pos))
                        file.write('\n')
                        sfEventCount = sfEventCount + 1
                    file.close()
                    print("\nProgram saved successfully! Choose this option (y) again to execute your program.")
                else:
                    recs = {}
                    for event in events:
                        if event.type == 'R':
                            if event.name.split('.')[-1] == "pkr":
                                recs[event.name] = seqExt.fileToPKR(event.name)
                            elif event.name.split('.')[-1] == "pmr":
                                recs[event.name] = seqExt.fileToPMR(event.name)
                    running = True
                    cycle = 1
                    timesToRun = "infinity" if loopAmnt < 0 else loopAmnt
                    print("Running program in 5")
                    seqExt.countdown()
                    while running:
                        print("\nRunning program for time " + str(cycle) + '/' + str(timesToRun))
                        for event in events:
                            if event.type == 'W':
                                print("Waiting for " + str(event.seconds) + " seconds")
                                time.sleep(event.seconds)
                            elif event.type == 'R':
                                subCycle = 1
                                subRunning = True
                                while subRunning:
                                    print("Playing '" + event.name + "' for time " + str(subCycle) + '/' + str(int(event.playCount)))
                                    if event.name.split('.')[-1] == "pkr":
                                        keyboard.play(recs[event.name])
                                    elif event.name.split('.')[-1] == "pmr":
                                        mouse.play(recs[event.name])
                                    if subCycle == event.playCount: subRunning = False
                                    subCycle+=1
                            elif event.type == 'M':
                                if event.meType == "click":
                                    print("Left-Clicking")
                                    mouse.click()
                                elif event.meType == "press":
                                    print("Holding left-click")
                                    mouse.press(button="left")
                                elif event.meType == "release":
                                    print("Releasing left-click")
                                    mouse.release(button="left")
                                elif event.meType == "move":
                                    print("Moving mouse arrow to " + str(event.pos))
                                    mouse.move(event.pos[0], event.pos[1], 1)
                        if cycle == timesToRun: running = False
                        cycle+=1
print("\nGoodbye for now!")
