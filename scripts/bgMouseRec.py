#This script is run in the background from the main (sequencer.py) script and is used when recording both mouse and keyboard and playing them both back at the same time.
from time import sleep, time
from mouse import record
from seqExt import PMRtoFile
file = open("local/sync.sqs", "a+")
file.seek(0,0)
lines = file.readlines()
file.close()
responded = False
while responded == False:
    print("Waiting for start time")
    if lines != []:
        file = open("local/sync.sqs", "a+") #SeQuencer Settings
        file.write("\nSTART TIME RECEIVED")
        file.close()
        responded = True
        print("Wrote 'START TIME RECEIVED' in sync.sqs")
    else:
        sleep(1)
pmr = []
print("Waiting to start recording")
while pmr == []:
    if time() >= float(lines[0]):
        print("Recording...")
        pmr = record(button="middle")
        print("Finished recording")
waitingToSave = True
while waitingToSave:
    print("Waiting to save")
    file = open("local/sync.sqs", 'r')
    lines = file.readlines()
    file.close()
    if len(lines) == 3:
        print("Saving as " + lines[2])
        file = open("local/recordings/" + lines[2], 'a')
        file.write("*!~!*\n")
        file.close()
        PMRtoFile(pmr, "local/recordings/" + lines[2], "kmr")
        file = open("local/sync.sqs", 'a')
        file.write("\nFILE NAME RECEIVED")
        file.close()
        waitingToSave = False
    sleep(2)
print("Saved and at end of program")
