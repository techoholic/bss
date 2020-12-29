from playsound import playsound
from win10toast import ToastNotifier
from pynput.keyboard import Listener, Key
import time
import datetime
file = open("local/events.pri", 'r')
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
        if line.split('/')[2] != '\n':
            timeFromStr = datetime.datetime.strptime(line.split('/')[2].split('\n')[0], "%Y-%m-%d %H:%M:%S.%f")
        events[group].append([line.split('/')[0], line.split('/')[1], timeFromStr])
print(events)
groupChars = {}
for grp in events:
    groupChars[grp.split('/')[1][0].lower()] = grp
#print(groupChars)
toaster = ToastNotifier()
toaster.show_toast("Reminder.py is active!", "The script is now running in the background; run reminderConsole.bat for more options", duration=6)
alt = False
grpKey = ''
lastChecked = 0
eventsReady = []
def on_press(key):
    global alt, groupChars, grpKey, lastChecked
    print("Key pressed: {0}".format(key))
    if (time.time() - lastChecked) > 60:
        eventsReadyLT = len(eventsReady)
        for group in events:
            for event in events[group]:
                if event[2]:
                    if datetime.datetime.now() > event[2] and event[0] not in eventsReady:
                        eventsReady.append(group + '/' + event[0])
        if eventsReady:
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
            if event[2] != '\n':
                if datetime.datetime.now() > event[2]:
                    ready2claim = True
            if not event[2] or ready2claim:
                if 'h' in event[1]:
                    timeFormatting = event[1].split('h')[0] + " hours"
                elif 'm' in event[1]:
                    timeFormatting = event[1].split('m')[0] + " minutes"
                toaster.show_toast(groupChars[grpKey] + '/' + event[0] + " claimed!", "Ready again in " + timeFormatting, duration=7, threaded=True)
                events[groupChars[grpKey]][2] = datetime.datetime.now()
                file = open("local/events.pri", 'w')
                file.write("#PYTHON REMINDER INFO\n\n")
                for group in events:
                    file.write('~' + group + "~\n")
                    for event in events[group]:
                        if '\n' in event[1]:
                            event[1] = event[1].split('\n')[0]
                        file.write(event[0] + '/' + event[1] + '/' + str(event[2]) + '\n')
                    file.write('\n')
                file.close()
            elif event[2]:
                #say how much time is left to claim
                delta = event[2] - datetime.datetime.now()
                hrsLeft = int(delta.seconds/3600)
                minsLeft = int(delta.seconds-hrsLeft*60)
                timeFormatting = (str(hrsLeft) + "hrs " if hrsLeft else '') + str(int(minsLeft)) + ("mins" if hrsLeft else " minutes")
                toaster.show_toast(groupChars[grpKey] + '/' + event[0] + " not ready yet", "Ready in " + timeFormatting, duration=7, threaded=True)

            mins = 1
            if events[groupChars[grpKey]][(int(key.char)-1)][2]:
                delta = datetime.datetime.now() - events[groupChars[grpKey]][(int(key.char)-1)][2]
                if 'h' in events[groupChars[grpKey]][(int(key.char)-1)][1]:
                    factor = 60
                    unit = 'h'
                elif 'm' in events[groupChars[grpKey]][(int(key.char)-1)][1]:
                    factor = 3600
                    unit = 'm'
                mins = float(events[groupChars[grpKey]][(int(key.char)-1)][1].split(unit)[0])*factor
            if (int(key.char) <= len(events[groupChars[grpKey]]) and int(key.char) > 0) or mins < 1:
                if not events[groupChars[grpKey]][(int(key.char)-1)][2]:
                    if 'h' in events[groupChars[grpKey]][(int(key.char)-1)][1]:
                        timeFormatting = events[groupChars[grpKey]][(int(key.char)-1)][1].split('h')[0] + " hours"
                    elif 'm' in events[groupChars[grpKey]][(int(key.char)-1)][1]:
                        timeFormatting = events[groupChars[grpKey]][(int(key.char)-1)][1].split('m')[0] + " minutes"
                    toaster.show_toast(groupChars[grpKey] + '/' + events[groupChars[grpKey]][(int(key.char)-1)][0] + " claimed!", "Ready again in " + timeFormatting, duration=7, threaded=True)
                    now = datetime.datetime.now()
                    events[groupChars[grpKey]][(int(key.char)-1)][2] = now
                    file = open("local/events.pri", 'w')
                    file.write("#PYTHON REMINDER INFO\n\n")
                    for group in events:
                        file.write('~' + group + "~\n")
                        for event in events[group]:
                            if '\n' in event[1]:
                                event[1] = event[1].split('\n')[0]
                            file.write(event[0] + '/' + event[1] + '/' + str(event[2]) + '\n')
                        file.write('\n')
                    file.close()
                else:
                    print("The else is running")
                    delta = datetime.datetime.now() - events[groupChars[grpKey]][(int(key.char)-1)][2]
                    if 'h' in events[groupChars[grpKey]][(int(key.char)-1)][1]:
                        factor = 60
                        unit = 'h'
                    elif 'm' in events[groupChars[grpKey]][(int(key.char)-1)][1]:
                        factor = 3600
                        unit = 'm'
                    mins = float(events[groupChars[grpKey]][(int(key.char)-1)][1].split(unit)[0])*factor
                    totalMinsLeft = mins - int(delta.seconds/60)
                    hoursLeft = int(totalMinsLeft/60)
                    minsLeft = totalMinsLeft-60*hoursLeft
                    timeFormatting = (str(hoursLeft) + "hrs " if hoursLeft else '') + str(int(minsLeft)) + ("mins" if hoursLeft else " minutes")
                    toaster.show_toast(groupChars[grpKey] + '/' + events[groupChars[grpKey]][(int(key.char)-1)][0] + " not ready yet", "Ready in " + timeFormatting, duration=7, threaded=True)
                    print("Are we getting here??")
                grpKeyPressed = False
                grpKey = ''
    elif alt:
        try:
            if key.char in groupChars:
                grpKey = key.char
        except AttributeError:
            grpKey = ''
        else:
            if key.char == 'm':
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
