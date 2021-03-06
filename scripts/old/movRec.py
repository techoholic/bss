import keyboard
import time
print("This scripts records your movement sequences and saves them in a file")
print("Press ` to start the recording countdown")
keyboard.wait('`')
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
working = True
while (working):
    print("p. Playback you recording")
    print("s. Save the recording as a file to be accessed later")
    print("`. Discard your recording and start a new one")
    option = input("Type p, s, x, or ` (tilde) and then press enter: ")
    if (option == '``p' or option == 'p'):
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
        keyboard.play(movSeq)
    elif (option == '``s' or option == 's'):
        name = input("What do you want to name this movSeq? ")
        file = open("local/movSeqs/" + name, "w")
        file.writelines(str(movSeq))
        file.close()
    elif (option == '```' or option == '`'):
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
