#!/usr/bin/env python
from pygame import mixer
from pydub import AudioSegment
import time

def playBell():
    song = AudioSegment.from_mp3("sounds/prebell.mp3")
    newsong = song.export("sounds/prebell.wav", format="wav")

    mixer.init()
    sound = mixer.Sound(file="sounds/prebell.wav")
    sound.play()
    time.sleep(6)
    mixer.quit()

playBell()
