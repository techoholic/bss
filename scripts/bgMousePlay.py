from time import sleep, time
from mouse import play
from seqExt import KMRtoRec
file = open("local/sync.sqs", 'r')
nameOfFile = file.read()
file.close()
startTime = time() + 5
file = open("local/sync.sqs", 'a')
file.write("\n" + str(startTime))
file.close()
pmr = KMRtoRec(nameOfFile, "pmr")
waitingToPlay = True
while waitingToPlay:
    if startTime <= time():
        play(pmr)
        waitingToPlay = False
