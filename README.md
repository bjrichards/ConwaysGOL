# Recreation of Conway's Game of Life

## Purpose
Created as a prototype to experience the challenges that come with creating this game. The knowledge gained from this will be applied to the 3-dimensional two-player strategy game currently being created for my CS 480 graphics class in C++ and OpenGl.

## Important Notes
Since TKinter is only fully supported by Windows and MacOS, this program will flicker each frame if ran on a Linux based OS. This is due to the call used to complete all idle tasks in TKinter not functioning correctly when running on a Linux distro. 

Therefore, this program is only tested and supported for Windows and MacOS.

## Requirements
```
Python3
TKinter
```

## To Do
This program was written quickly as a prototype, therefore it lacks commenting, strong structuring, and is not optimized in any way. So, over time when I have free time I will be cleaning up the code, adding comments when needed, and working to increase framerates/generation rates when the number of cells (and therefore the number of drawn objects) reach a high number.
