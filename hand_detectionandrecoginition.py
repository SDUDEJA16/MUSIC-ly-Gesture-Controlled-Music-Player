import cv2
import numpy as np
import math
import os
import pygame #play music
from tkinter.filedialog import askdirectory
from tkinter import *

root=Tk()
root.configure(background='grey')
root.minsize(300,300)
listofsongs = []
total=3
index = total-1#of list
def nextsong(event):
    global index
    if(index==0):
        index=total-1
    else:
        index-=1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
   
def stopsong(event):
     pygame.mixer.music.stop()
     
def directorychooser():
    directory = askdirectory()
    os.chdir(directory)#change directory

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            listofsongs.append(files)
  
    print(listofsongs)

    
    
    pygame.mixer.init()#initialise mixer module
def nextsong():
    
    global index
    if(index==0):
        index=total-1
    else:
        index-=1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
def stopsong():
    pygame.mixer.music.stop()
def prevsong():
    global index
    index+=1
    index=index%total
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()

def playsong():
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()    
directorychooser()
#listofsongs.reverse()
label=Label(root, text='Music Player',font=('times', 10, 'bold'), bg='grey')
label.pack()
listbox = Listbox(root,font=('times', 10, 'bold'),width=25, bg='white')
listbox.pack()
for items in listofsongs:
    listbox.insert(0,items)
nextbutton=Button(root,activebackground='white',activeforeground='blue',font=('times', 9),text='Next Song',width=10)
nextbutton.pack()
previousbutton=Button(root,activebackground='white',activeforeground='blue',font=('times', 9),text='Previous Song',width=10)
previousbutton.pack()
stopbutton=Button(root,activebackground='white',activeforeground='blue',font=('times', 9),text='Stop',width=10)
stopbutton.pack()
playbutton=Button(root,activebackground='white',activeforeground='blue',font=('times', 9),text='Play',width=10)
playbutton.pack()

nextbutton.bind("<Button-1>",nextsong)#<Button-1> left button
#<Button-2> wheel
#3 is right
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)
playbutton.bind("<Button-1>",playsong)

cap=cv2.VideoCapture(0)
while(cap.isOpened()):
    ret,img=cap.read()
    
    cv2.rectangle(img,(0,0),(350,350),(0,255,),0)
    crop=img[0:350,0:350]#roi
    
    grey=cv2.cvtColor(crop,cv2.COLOR_BGR2GRAY)
    
    value=(35,35)
    blur=cv2.GaussianBlur(grey,value,0)
    ret1,thresh=cv2.threshold(blur,127,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    contours, hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)#cv2.CHAIN_APPROX_SIMPLE
    drawing = np.zeros(crop.shape,np.uint8) 

    cnt = max(contours, key = lambda x: cv2.contourArea(x))
    
    hull=cv2.convexHull(cnt)
    areahull = cv2.contourArea(hull)
    areacnt = cv2.contourArea(cnt)
    arearatio=((areahull-areacnt)/areacnt)*100

    cv2.drawContours(drawing,[cnt],0,(0,255,0),0)
    cv2.drawContours(drawing,[hull],0,(0,0,255),0)

    hull=cv2.convexHull(cnt, returnPoints=False)

    defects = cv2.convexityDefects(cnt, hull)
    count_defects = 0
    cv2.drawContours(thresh, contours, -1, (0, 255, 0), 3)#3 is width
    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]#[start point, end point, farthest point, approximate distance to farthest point ].
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
    # find length of all sides of triangle

        a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)

        b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)

        c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)



        # apply cosine rule here

        angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57



        # ignore angles > 90 and highlight rest with red dots

        if angle <= 90:

            count_defects += 1

            cv2.circle(crop, far, 1, [0,0,255], -1)

    # define actions required

    if count_defects == 1:

        cv2.putText(img,"2", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255), 2)
        

    elif count_defects == 2:
        str = "2"
        cv2.putText(img, "3", (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255), 2)
        

    elif count_defects == 3:

        cv2.putText(img,"4", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255), 2)
        playsong()

    elif count_defects == 4:

        cv2.putText(img,"5", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255), 2)
        stopsong()

    else:
        if areacnt<2000:
            cv2.putText(img,'Nothing',(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),1,cv2.LINE_AA)    
        else:
            if arearatio<12:
                cv2.putText(img,'0',(50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 3, cv2.LINE_AA)
                
            else:
                cv2.putText(img,'1',(50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 3, cv2.LINE_AA)
                
    cv2.imshow('thresh',thresh)
    cv2.imshow('frame',img)
    k = cv2.waitKey(10)
    
    if k == 27:
        break

    
cap.release()
cv2.destroyAllWindows()
