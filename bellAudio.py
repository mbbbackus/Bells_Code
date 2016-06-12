#!/usr/bin/env python
from pygame import mixer
from pydub import AudioSegment
import time
import constants

def convertAudio(audioPath):
    #path is a string, getting extension substring
    length = len(audioPath)
    ext = audioPath[length - 3:]
    wavPath = audioPath[:length-4]+".wav"
    #if it's mp3, convert; wav, do nothing; else, cancel
    if ext == 'mp3':
        s = AudioSegment.from_mp3(audioPath)
        s.export(wavPath, format="wav")
    elif ext == 'wav':
        pass
    else:
        return None
    return wavPath

def playBell(name, t):
    mixer.init()
    print name
    sound = mixer.Sound(name)
    sound.play()
    time.sleep(t)
    mixer.quit()

def playPrebell():
    path = constants.prebellPath
    playBell(path, 6)

def playPostbell():
    path = constants.prebellPath
    playBell(path, 18)

def playEmptybell():
    path = constants.prebellPath
    playBell(path, 306)
    playBell(path, 6)
