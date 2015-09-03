#!/usr/bin/env python
import json
from datetime import datetime
from os import listdir
import constants
import bell

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
    weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday']
    weekday = weekdays[int(today.weekday())]
    schedule = week_schedule[weekday]
    return schedule

def run_bells():
    #songs = loadSongs()
    schedule = loadSchedule(constants.schedulePath)
    while True:
        today = datetime.today()
        min_str = None
        if today.minute < 10:
            min_str = '0' + str(today.minute)
        else:
            min_str = str(today.minute)
        curtime = str(today.hour) + ':' + min_str
        for block in schedule:
            time = schedule[block]["Time"]
            if time == curtime:
                song = str(schedule[block]["song"])
                newbell = bell.Bell(song)
                newbell.play()

run_bells()