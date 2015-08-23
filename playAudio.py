#!/usr/bin/env python
from pygame import mixer
from pydub import AudioSegment
import time
import constants

def playBell(name, t):
    mixer.init()
    sound = mixer.Sound(file=name)
    sound.play()
    time.sleep(t)
    mixer.quit()

def playPrebell():
    path = constants.prebellPath
    playBell(path,6)

def playPostbell():
    path = constants.postbellPath
    playBell(path,18)

print "pre"
playPrebell()
print "post"
playPostbell()
