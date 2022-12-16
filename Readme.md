# **Title: MUSIC-ly - Gesture Controlled Music Player**

## **1. Project Objective**

Project's Main motive is to provide a convenient way to control a music player via some hand gestures and somewhere eradicating the use of keyboard or touchpad to play pause an audio file in a personal computer. Sincetechnology provides more convenient ways to fulfill or perform the tasks more easily and efficiently therefore the idea of this project is to ease the control panel of an audio player.

## **2. Introduction to Tools and Technology**

Python was used for the designing the project as it is high level and dynamic programming language. It emphasizes code readability and also helps in optimizing the size of code

* #### __Python code Execution__ ####

The source code is translated to byte code, which is then run by the python virtual machine and then automatically compiled and then interpreted.

![interpreter](Screenshot%20(1284).png)

## **3. Python Packages Used**

* ### openCV - It is an open source computer vision library used for real time image processing. 
* ### pygame - This module is just used for playing the mp3 music in the music player. "mixer.music" method is used for loading the playing the music.
* ### mutagen - It is for handling the metadeta of music files. To display the title of the song
* ### tkinter - It was for creating the basic GUI of the system to manually control the music player.

## **4.Methadology** ## 

OpenCV is a open source library used for the real time Image processing.

Now for the Hand Detection mainly two methods are most popular

* On the basis of `Skin Colour Detection`
* On the basis of `Convexity Detection`

First of all, Binary mask of the hand is created with the help of one of above mentioned methods.
In this I have used the method of Skin Colour detection.

In Binary mask, the region belonging to hand is marked as 1 and rest as 0.Mask is then smoothened and all the noise is removed.

***
![method](Blank%20diagram%20(5).jpeg)

## **5.Screenshots of the Interface** ## 
***

![screenshots](Screenshot%20(1289).png)
Selecting mp3 music folder
***
![screenshots](Screenshot%20(1290).png)
***
![screenshots](Screenshot%20(1291).png)
***
![screenshots](Screenshot%20(1292).png)
Binary mask of hand
***
![screenshots](Screenshot%20(1294).png)
Finger Tips detection

