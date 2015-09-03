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
        for m in music:
            if m == self.name:
                self.song_path = constants.musicPath + self.name
        self.path = bellAudio.convertAudio(self.song_path)
        song = AudioSegment.from_wav(self.path)
        self.length = (len(song) / 1000) + 1
    def play(self):
        if self.song_path == None:
            return
        bellAudio.playPrebell()
        bellAudio.playBell(self.path, self.length)
        bellAudio.playPostbell()

#newbell = Bell("Keep your money.mp3")
#newbell.play()