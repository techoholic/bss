import keyboard
import
print("This scripts records your movements and saves them in a '.txt' file")
print("Press ` to start and then again to stop")
keyboard.wait('`')
print("Recording session started. Type away!")
movement = keyboard.record(until='`')
print("Recording session ended. Press 'space' to play back the movement sequence")
keyboard.wait('space')
keyboard.play(movement)
