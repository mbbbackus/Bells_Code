#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
import json
from datetime import datetime
from os import listdir
import constants
import bell
import bellAudio

def loadSongs():
    path = constants.musicPath
    musicDir = listdir(path)
    music = []
    for m in musicDir:
        ext = m[len(m)-4:]
        if ext == "wav":
            music.append(m)
    return music

def loadSchedule(sched):
    #schedule is an example of schedule.json
    json_file = open(sched)
    week_schedule = json.load(json_file)
    json_file.close()

    today = datetime.today()
    #day, monday = 0, sunday = 6
    weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    weekday = weekdays[int(today.weekday())]
    schedule = week_schedule[weekday]
    return schedule

def run_bells():
    #songs = loadSongs()
    while True:
        today = datetime.today()
    	schedule = loadSchedule(constants.schedulePath)
        min_str = None
        if today.minute < 10:
            min_str = '0' + str(today.minute)
        else:
            min_str = str(today.minute)
        curtime = str(today.hour) + ':' + min_str
        for block in schedule:
            time = schedule[block]["Time"]
            if time == curtime:
		try:
                    song = str(schedule[block]["song"])
                    newbell = bell.Bell(song)
                    newbell.play()
		except IOError:
		    bellAudio.playEmptybell()

run_bells()
