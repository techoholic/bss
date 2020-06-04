import keyboard
print("This scripts records your movement sequences and saves them in a file")
print("Press ` to start and then again to stop")
keyboard.wait('`')
print("Recording session started. Press ` to stop")
movSeq = keyboard.record(until='`')
print("Recording session ended. What do you want to do now?")
option = ''
while (option = ''):
    print("p. Playback you recording")
    print("s. Save the recording as a file to be accessed later")
    print("x. Delete the recording")
    print("`. Discard your recording and start a new one")
    option = input("Type p, s, x, or ` (tilde) and then press enter: ")
    if (option == '``p' or option == 'p'):
        keyboard.play(movSeq)
