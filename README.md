Subtitles
============
_____________
Python program that automatically create subtitles for a video!
______________
Dependencies:
--------------
__pip installations__  
`pip install -r requirements.txt`

__Vlc__  
Vlc installed on your device.  
You can download at https://www.videolan.org/

__Ffmpeg__  
Ffmpeg must be installed on your device.  
You can download at https://ffmpeg.org/download.html

_____________________
Usage
----------
__Input__  
Place input video as `input.mp4` in `input` folder.  
Place wanted subtitles in line-separated file at `subtitles.txt` in `input` folder.

__Running__  
Double click `main.py` or use cmd `python3 main.py`.  
Split the video window and the command window in a way that is most comfortable to you.  
Press any key to start the video. The subtitles will be played along with the video.  
every enter that is pressed will save the subtitle that is currently on the screen and move on to the next one.


__Configuration__  
The input and output files can be changed via the configuration file in `cofiguration.configuration.py`.  
Set the directory for files and file names by changing the values in the configuration.

_______________________

Notes
======
__Last Enter press__  
On a terminal that supports interactive shell, the video screen will close automatically when the video ends.  
On the other hand, if the shell is not interactive, the user must hit enter one more time at the end of the video
in order to move to the conversion step.

________________

Enjoy!
