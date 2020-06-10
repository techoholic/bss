import keyboard
import time
print("Welcome to the Ultimate Bee Swarm Simulator Script v1.0!")
print("a. Move in a square (variable)")
print("c. Run a saved movSeq (don't use this!!!)")
option = input("Type 'a' or 'b' and press Enter: ")
if (option == 'a'):
    time.sleep(0.5)
    waitTime = input("\nHow many seconds between press and release (0.8 is default): ")
    waitTime = float(waitTime)
    print("Waiting for 5 seconds...")
    time.sleep(5)
    print("Starting the script!")
    running = True
    while(running):
        keyboard.press('w')
        time.sleep(waitTime)
        keyboard.release('w')
        keyboard.press('a')
        time.sleep(waitTime)
        keyboard.release('a')
        keyboard.press('s')
        time.sleep(waitTime)
        keyboard.release('s')
        keyboard.press('d')
        time.sleep(waitTime)
        keyboard.release('d')
elif (option == 'c'):
    files = os.listdir("local/movSeqs/")
    i = 0
    for filename in files:
        print(i, ". ", filename, sep='')
        i = i + 1
    fto = input("Type the number of the movSeq you want to run and press enter: ") #file to open
    filename = files[int(fto)]
    file = 'gotta come back to this later'
    keyboard.play()
