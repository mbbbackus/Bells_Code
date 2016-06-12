Potomac School Bells Code Documentation
Ben Backus – mbbbackus@gmail.com
May 19, 2016

PTS Bells Code runs on python v2.7.0
Two external libraries are used:
	Pygame
		This library provides easy access to playing audio with the mixer class
		mixer provides a function that can play a sound file given its path
		Pygame docs: http://www.pygame.org/docs/
		
	Pydub
		Pydub is used for standardizing the audio files to wav files
		Pygame handles wav files best, but handles mp3s poorly
		While users are allowed to use mp3 files, the audio is converted to wav format
		before being played so that the mixer function from pygame can use it
		Pydub docs: http://pydub.com/
		
The Bells code is essentially composed of five important files
The general overview goes:
	bell.py
		Defines the Bell class
	bellAudio.py
		Defines Audio conversion function and bell-playing functions
	main.py
		Executable file that runs the bells code
	constants.py
		Defines constants used elsewhere in code
	default_lol.json
		json file parsed by main.py to run bells on schedule 
		
Additionally, there is a music directory that contains the bells songs


-----------------------------------------------------------------------------------------
constants.py
-----------------------------------------------------------------------------------------

This file defines five variables:

projPath: the path to the directory containing the bells code; calls sys.path (sys is from
general python library)

prebellPath: path to the prebell file

postbellPath: path to postbell file

(The difference between postbell and prebell is that prebell plays one chime, the postbell
plays three chimes – the postbell isn't used anymore but the option is still there)

musicPath: path to the music directory

schedulePath: path to the schedule file (currently default_lol.json)


-----------------------------------------------------------------------------------------
default_lol.json
-----------------------------------------------------------------------------------------

This json file organizes the bell schedule for one week
Since json can be easily converted into a dictionary in python (which is similar to a map
in Java), the contents of this file are parsed by the main file on a continous loop

The hierarchy of the file is: weekday - block - time/song

The Json should be formatted as such:
(ellipses represent blocks that aren't shown for concision sake)

{
	"Monday":
	{
		"B_block"    : {"Time": "8:05", "song": "SongPath/SongFile.mp3"},
		"A_block"    : {"Time": "8:55", "song": "SongPath/SongFile.mp3"},
		"Conference" : {"Time": "9:40", "song": "SongPath/SongFile.mp3"},
		"G_block"    : {"Time": "10:20", "song": "SongPath/SongFile.mp3"},
		"H_block"    : {"Time": "11:05", "song": "SongPath/SongFile.mp3"},
		"E_block"    : {"Time": "11:50", "song": "SongPath/SongFile.mp3"},
		"F_block"    : {"Time": "12:35", "song": "SongPath/SongFile.mp3"},
		"D_block"    : {"Time": "13:20", "song": "SongPath/SongFile.mp3"},
		"Break"      : {"Time": "14:05", "song": "SongPath/SongFile.mp3"},
		"C_block"    : {"Time": "14:25", "song": "SongPath/SongFile.mp3"},
		"End"        : {"Time": "15:10", "song": "SongPath/SongFile.mp3"}
	},
	"Tuesday": 
	{
		"B_block"    : {"Time": "8:05", "song": "SongPath/SongFile.mp3"},
		...
		"End"        : {"Time": "15:10", "song": "SongPath/SongFile.mp3"}
	},
	"Wednesday":
	{
		"A_block" : {"Time": "8:05", "song": "SongPath/SongFile.mp3"},
		...
		"End"        : {"Time": "15:10", "song": "SongPath/SongFile.mp3"}
	},
	"Thursday":
	{
		"A_block" : {"Time": "8:05", "song": "SongPath/SongFile.mp3"},
		...
		"End"        : {"Time": "15:10", "song": "SongPath/SongFile.mp3"}
	},
	"Friday": 
	{
		"A_block"     : {"Time": "8:05", "song": "SongPath/SongFile.mp3"},
		...
		"End"        : {"Time": "15:10", "song": "SongPath/SongFile.mp3"}

    }
}

It is suggested that all json be validated via https://jsonformatter.curiousconcept.com/
in order to ensure that the code will run


-----------------------------------------------------------------------------------------
bellAudio.py
-----------------------------------------------------------------------------------------

Five functions:
	convertAudio
	playBell
	playPrebell
	playPostbell
	playEmptybell
	
convertAudio:
takes one parameter, audioPath, which is the path of the file being converted
the function checks the extension of the file: 
	if wav, it returns the original file path
	if mp3, it creates a new file that is in wav format, then returns that file's path
	else, it returns None
	
playbell:
takes two parameters:
	name - the file path of the song
	t - the length of the song in seconds
playbell initializes mixer to play the sound, then the program sleeps for t seconds

playPrebell and playPostbell:
no parameters, call the playBell function with the bell chimes as parameters 

playEmptybell:
no parameters, calls playBell function with prebell path and 5 minutes as paramaters,
rather than playing music, then plays another bell chime
Essentially this function plays two bell chimes with a 5 minute gap in between


-----------------------------------------------------------------------------------------
bell.py
-----------------------------------------------------------------------------------------

Bell Class:
One parameter, n, which is the path of the song from within the music directory
	Ex. if full song path is /Users/bells/Documents/bells/Bells_Code/music/song/songpath
	then n is: song/songpath
	This is just in case the bells code is ever moved so that the code can survive being
	moved to another location on the computer
	
Four initial variables:
	self.name = n
	self.song_path - initialized as None but later defined as the full path to the song
	self.path - the new path once the file has been converted
	self.length - length of the song in seconds 
	
play:
	no parameters, if the song file exists and was entered into the json correctly, it is
	played along with the bell chimes for 5 minutes (300 is param for 300 seconds)
	

-----------------------------------------------------------------------------------------
main.py
-----------------------------------------------------------------------------------------

three functions:
	loadSongs - deprecated
	loadSchedule
	run_bells
	
loadSchedule:
converts default_lol.json into dictionary
returns subdictionary corresponding to the weekday

run_bells:
begins infinite while loop that runs until program is cancelled
in each iteration of loop:
	calls loadSchedule
	converts python datetime object to a string comparable to the time values from the
		json file (Ex. "Time":"15:10" for 3:10 pm)
	compares current time to every time value in the schedule
	if any of the times match the current time:
		initializes new Bell object with the parameter being the song in the corresponding
			line of json info
		if the song wasn't input properly or can't be played for some reason the 
			playEmptyBell function is called
			
at the end of the file, the run_bells function is called


-----------------------------------------------------------------------------------------
additionally info
-----------------------------------------------------------------------------------------

should the code be moved to another computer, potential issues and solutions are as such:
	main.py isn't executable
		can be solved by using the chmod command in terminal to make file executable
		Ex. :Bells_Code bells$ sudo chmod +x main.py 
			then enter root password
		You can check the files privileges with ls -l while in the code's directory
		
	pygame isn't working; receiving errors on 'import python'
		Ensure python is on v2.7.0
			might require uninstalling python completely, then installing correct version
		Ensure pygame is installed correctly, reinstall with pip
	
	pydub isn't working; pydub related errors
		don't redownload pydub, first try changing the python line (#!/usr/bin/env python)
			at the top of each line, ensure that this is the correct path to python on
			comp, if python path is actually different then change it
		Worst case scenario, remove instances of pydub and convert all files to wav format
			before inputting to json 
	
	General solution: reinstall python 2.7.0, but only once every instance has been
		completely uninstalled
		
	This won't run on windows, don't do that
		
	