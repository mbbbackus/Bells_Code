Bells Code
Repository to contain source for Bells program that plays songs between classes during school day

Dependencies:
    Pygame
    Pydub
    

File explanations:

    bellAudio.py:
        8/22/15 - contains playPrebell function that plays the prebell
        8/24/15 - prebell and postbell, plus playbell to play any song
    
    convertAudio.py:
        8/24/15 - converts mp3 to wav
        
    bell.py:
        8/24/15 - class that plays prebell, song, then postbell
    
    constants.py:
        8/24/15 - variables constants library
    
    sounds directory:
        Contains prebell and other music files, converted files also go here
    
    pydub directory:
        External Library used to convert music files to wav format for pygame module
