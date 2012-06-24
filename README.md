muscovaudio
===========

Death's-head Hawkmoth

A project by Emma & Parham

WHAT YOU NEED:  
To run Muscovaudio you need to have the following python libraries:
* Pygame (that requires SDL)
* pyOSC
* numpy (part of pygame requires numpy)
* python 2.7

Use [pip](http://pypi.python.org/pypi/pip) to install numpy and pyOSC. Follow instructions on Pygame's [website](http://pygame.org/download.shtml) to install it for your platform. 

Muscovaudio was developed against python 2.7 and to get all the dependencies to run on Mac OS X 10.6 (Snow Leopard) do as above but to install Pygame you can read the instructions here: http://www.shodanproductions.com/forum/viewtopic.php?t=67&p=272#p272 (found on http://pygame.org/wiki/MacCompile).  

HOW TO USE MUSCOVAUDIO:  
You will need Python 2.7, Pure Data and Simple Synth (or the equivalent). 

1 ) Downloada and unzip the latest zip from https://github.com/parhamfh/muscovaudio/tags  
2 ) Open Simple Synth.  
3 ) Open Pure Data and launch the pd patch called "main.py".  
4) Make sure that Audio and MIDI is on in Pure Data. Go to Preferences/MIDI Settings… and choose Simple Synth as MIDI output. 
5) Run ```python muscovaudio.py``` from the terminal and enjoy the craziness!  

You can draw lines using the mouse, thereby making balls collide. When the balls collide with each other, you can hear sounds. :) 
