import keyboard
import time
import math
print("Welcome to the Ultimate Bee Swarm Simulator Script v1.0!")
time.sleep(0.5)
print("Waiting for 5 seconds...")
time.sleep(5)
print("Starting the script!")
running = True
while(running):
    keyboard.press('w')
    time.sleep(0.8)
    keyboard.release('w')
    keyboard.press('a')
    time.sleep(0.8)
    keyboard.release('a')
    keyboard.press('s')
    time.sleep(0.8)
    keyboard.release('s')
    keyboard.press('d')
    time.sleep(0.8)
    keyboard.release('d')
