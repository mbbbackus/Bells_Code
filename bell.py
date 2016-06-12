#!/usr/bin/env python
import bellAudio
import constants
from os import listdir
from pydub import AudioSegment

class Bell:
    def __init__(self, n):
        self.name = n
        self.song_path = None
        music = listdir(constants.musicPath)
        self.song_path = constants.musicPath + self.name
	self.path = bellAudio.convertAudio(self.song_path)
        song = AudioSegment.from_wav(self.path)
        self.length = (len(song) / 1000) + 1
    def play(self):
        if self.song_path == None:
            return
        bellAudio.playPrebell()
        bellAudio.playBell(self.path, 300)
        bellAudio.playPostbell()

#newbell = Bell("A Perfect Circle/Sleeping Beauty.mp3")
#newbell.play()
