#!/usr/bin/env python
from pydub import AudioSegment
import constants
import sys

songpath = sys.argv[1]
song = AudioSegment.from_wav(songpath)
print float(len(song)) / 1000
