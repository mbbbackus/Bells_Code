#!/usr/bin/env python
import bellAudio
import constants
from os import listdir

class Bell:
    def __init__(self, n, l):
        self.name = n
        self.length = l
        self.song_path = None
        music = listdir(constants.musicPath)
        for m in music:
            if m == self.name:
                self.song_path = constants.musicPath + self.name
    def play(self):
        if self.song_path == None:
            return

        path = bellAudio.convertAudio(self.song_path)
        print path
        bellAudio.playPrebell()
        bellAudio.playBell(path, self.length)
        bellAudio.playPostbell()

newbell = Bell("Keep your money.wav", 30)
newbell.play()