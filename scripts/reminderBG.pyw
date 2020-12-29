from win10toast import ToastNotifier
from pynput.keyboard import Listener, Key
from seqExt import dirInit()
import time
import datetime
try:
    file = open("local/events.pri", 'r')
except:
    dirInit()
    file = open("global/events_template.pri", 'r')
lines = file.readlines()
file.close()
events = {}
for line in lines:
    if line[0] == '~':
        group = line.split('~')[1]
        events[group] = []
    elif line == '\n':
        group = ''
    elif line[0] != '#' and group:
        timeFromStr = ''
        if len(line.split('/')) == 3:
            if line.split('/')[2] != '\n':
                timeFromStr = datetime.datetime.strptime(line.split('/')[2].split('\n')[0], "%Y-%m-%d %H:%M:%S.%f")
        events[group].append([line.split('/')[0], line.split('/')[1], timeFromStr])
print(events)
groupChars = {}
for grp in events:
    groupChars[grp.split('/')[1][0].lower()] = grp
print(groupChars)
toaster = ToastNotifier()
toaster.show_toast("Reminder.py is active!", "The script is now running in the background; run reminderConsole.bat for more options", duration=6)
alt = False
grpKey = ''
lastChecked = 0
eventsReady = []
muted = False
def on_press(key):
    global alt, groupChars, grpKey, lastChecked, muted
    print("Key pressed: {0}".format(key))
    if (time.time() - lastChecked) > 60:
        eventsReadyLT = len(eventsReady)
        for group in events:
            for event in events[group]:
                if event[2]:
                    if datetime.datetime.now() > event[2] and group + '/' + event[0] not in eventsReady:
                        eventsReady.append(group + '/' + event[0])
        if eventsReady and not muted:
            grammar = " event is" if len(eventsReady) == 1 else " events are"
            grammarDesc = 's' if len(eventsReady) > 1 else ''
            toaster.show_toast(("[+" + str(len(eventsReady)-eventsReadyLT) + "] " if len(eventsReady) != eventsReadyLT else '') + str(len(eventsReady)) + grammar + " ready to claim!", "Event" + grammarDesc + ': ' + ''.join(event + ('' if event == eventsReady[-1] else ', ') for event in eventsReady), duration=12, threaded=True)
        lastChecked = time.time()
    if key == Key.alt_gr:
        alt = True
    elif grpKey and alt:
        try:
            int(key.char)
        except:
            grpKey = ''
        else:
            event = events[groupChars[grpKey]][(int(key.char)-1)]
            ready2claim = False
            if event[2]:
                if datetime.datetime.now() > event[2]:
                    ready2claim = True
            if not event[2] or ready2claim:
                if 'h' in event[1]:
                    timeFormatting = event[1].split('h')[0] + " hours"
                    mins = float(event[1].split('h')[0])*60
                elif 'm' in event[1]:
                    timeFormatting = event[1].split('m')[0] + " minutes"
                    mins = float(event[1].split('m')[0])
                toaster.show_toast(groupChars[grpKey] + '/' + event[0] + " claimed!", "Ready again in " + timeFormatting, duration=7, threaded=True)
                events[groupChars[grpKey]][(int(key.char)-1)][2] = datetime.datetime.now() + datetime.timedelta(minutes=mins)

                file = open("local/events.pri", 'w')
                file.write("#PYTHON REMINDER INFO\n\n")
                for group in events:
                    file.write('~' + group + "~\n")
                    for e in events[group]:
                        print(e)
                        if '\n' in e[1]:
                            e[1] = e[1].split('\n')[0]
                        file.write(e[0] + '/' + e[1] + '/' + str(e[2]) + '\n')
                    file.write('\n')
                file.close()
            elif event[2]:
                #say how much time is left to claim
                delta = event[2] - datetime.datetime.now()
                hrsLeft = int(delta.seconds/3600)
                minsLeft = int(delta.seconds/60-60*hrsLeft)
                timeFormatting = (str(hrsLeft) + "hrs " if hrsLeft else '') + (str(int(minsLeft)) + ("mins" if hrsLeft else " minutes") if minsLeft else str(delta.seconds) + " seconds")
                toaster.show_toast(groupChars[grpKey] + '/' + event[0] + " not ready yet", "Ready in " + timeFormatting, duration=7, threaded=True)
            grpKey = ''
    elif alt:
        try:
            if key.char in groupChars:
                grpKey = key.char
        except AttributeError:
            grpKey = ''
        else:
            if key.char == 'm':
                if muted:
                    muted = False
                    toaster.show_toast("Reminder.py is no longer muted", "You will now be sent a reminder about events to claim every minute", duration=12)
                else:
                    muted = True
                    toaster.show_toast("Reminder.py is now muted", "You will no longer be sent notifications for events to claim", duration=12)
            elif key.char == 'x':
                toaster.show_toast("Closing the script, goodbye!", "Thank you for using reminder.py :D", duration=12)
                return False
def on_release(key):
    global alt, grpKey
    print("Key released: {0}".format(key))
    if key == Key.alt_gr:
        alt = False
        grpKey = ''

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
