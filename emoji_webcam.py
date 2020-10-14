# -*- coding: utf-8 -*-
"""
Author: Maximilian Schrapel
Copyright: Copyright 2020, Webcam Augmentator
License: MIT
Version: 1.0.0
Email: maximilian.schrapel@gmail.com

This simple script allows you to add emojis to webcam streams independently from the video chat program.
Add the output window to a virtual camera via OBS Studio https://obsproject.com/ to use the software with any operating system and video chat.
Follow the steps of my tutorial to set up your webcam.
The emojis were taken from https://openmoji.org/

Press q to quit the program
Press 0 to 9 or - to add emoji
Press w to stop overlaying emojis

This code can help to show emotions with masks in video chats.
I have used parts of my code to teach my students how prototyping and AR can support wearing masks.
"""

import numpy as np
import cv2
import math

"""returns center of marker"""
def getCenter(prev_res):
    xm=0
    ym=0
    for i in range(0,4):
        ym+=prev_res[0][i][0]
        xm+=prev_res[0][i][1]
    xm=int(xm/4)
    ym=int(ym/4)
    center = (xm,ym)
    return center

"""returns size of marker"""
def getSize(res):
    size=0
    for i in range (0,4):
        size=max(size,math.sqrt((res[0][i][1]-res[0][(i+1)%4][1])**2 
                                + (res[0][i][0]-res[0][(i+1)%4][0])**2))    
    return size

"""returns image with overlayed emoji"""
def emojiOverlay(src , overlay , pos=(0,0),scale = 1):
    overlay = cv2.resize(overlay,(0,0),fx=scale,fy=scale)
    ax=0
    ay=0
    """go through image and add emoji"""
    for px in range(pos[0]-int(overlay.shape[0]/2),pos[0]+int(overlay.shape[0]/2)):
        for py in range(pos[1]-int(overlay.shape[1]/2),pos[1]+int(overlay.shape[1]/2)):
            if overlay[ax,ay].any()>0:
                if px>=0 and px<src.shape[0] and py>=0 and py <src.shape[1]:
                    src[px,py]=overlay[ax,ay]
            ay+=1
        ax+=1
        ay=0
    
    return src

"""find green marker to make motion smooth """
def isMarker(img , marker):
    minx=maxx=marker[0][0][1]
    miny=maxy=marker[0][0][0]
    for i in range (1,4):
        minx=min(minx,marker[0][i][1])
        maxx=max(maxx,marker[0][i][1])
        miny=min(miny,marker[0][i][0])
        maxy=max(maxy,marker[0][i][0])
    n=(maxx-minx)*(maxy-miny)
    count=0
    
    for x in range (int(minx),int(maxx)):
        for y in range (int(miny),int(maxy)):
            if img[x,y] > 0:
                count+=1
    greenshare=count/n
    return greenshare > 0.2

"""Opens webcam (set number according to your machine!)"""
cap = cv2.VideoCapture(0)
# stores the index of the selected emoji
imgindex = -1
"""Load emojis"""
img_emojilove=cv2.imread("Emojis/1F60D_color.png")
img_emojitogune=cv2.imread("Emojis/1F61B_color.png")
img_emojiteeth=cv2.imread("Emojis/1F62C_color.png")
img_emojicry=cv2.imread("Emojis/1F62D_color.png")
img_emojicrazy=cv2.imread("Emojis/1F92A_color.png")
img_emojimoulth=cv2.imread("Emojis/1F444_color.png")
img_emojihappy=cv2.imread("Emojis/1F600_color.png")
img_emojikiss=cv2.imread("Emojis/1F618_color.png")
img_emojiangry=cv2.imread("Emojis/1F620_color.png")
img_emojilol=cv2.imread("Emojis/1F923_color.png")
img_emojihot=cv2.imread("Emojis/1F975_color.png")


"""Resize emojis to 80x80 px"""
img_emojilove=cv2.resize(img_emojilove,(int(80),int(80)))
img_emojitogune=cv2.resize(img_emojitogune,(int(80),int(80)))
img_emojiteeth=cv2.resize(img_emojiteeth,(int(80),int(80)))
img_emojicry=cv2.resize(img_emojicry,(int(80),int(80)))
img_emojicrazy=cv2.resize(img_emojicrazy,(int(80),int(80)))
img_emojimoulth=cv2.resize(img_emojimoulth,(int(80),int(80)))
img_emojihappy=cv2.resize(img_emojihappy,(int(80),int(80)))
img_emojikiss=cv2.resize(img_emojikiss,(int(80),int(80)))
img_emojiangry=cv2.resize(img_emojiangry,(int(80),int(80)))
img_emojilol=cv2.resize(img_emojilol,(int(80),int(80)))
img_emojihot=cv2.resize(img_emojihot,(int(80),int(80)))


"""add emojis to dict"""
emojis= { i : [] for i in range(0,11) }
emojis[0]=img_emojilove
emojis[1]=img_emojitogune
emojis[2]=img_emojiteeth
emojis[3]=img_emojicry
emojis[4]=img_emojicrazy
emojis[5]=img_emojimoulth
emojis[6]=img_emojihappy
emojis[7]=img_emojikiss
emojis[8]=img_emojiangry
emojis[9]=img_emojilol
emojis[10]=img_emojihot

# stores the previous corners of the marker
prev_res=[]

"""Aruco markers"""
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters_create()
imgemoji= np.zeros([80,80,3])


"""starting loop ☺ """
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # detect markers
    res = cv2.aruco.detectMarkers(frame,dictionary)
    

    if imgindex == -1:
        img_emoji= np.zeros([80,80,3])
    else:
        for i in range(0,11):
            if imgindex==i:
                img_emoji=emojis[i]
                break

    """overlay emoji"""
    if len(res[0]) > 0 and imgindex != -1:
        for marker in res[0]:
            size_x = marker[0][0]
        
        # For debugging: show markers
        #cv2.aruco.drawDetectedMarkers(frame,res[0],res[1])

        # store result temporarly
        prev_res=res
        # find center position
        center=getCenter(prev_res[0][0])
        # add emoji to image
        scale=(getSize(prev_res[0][0])/80) * 3 
        frame=emojiOverlay(frame , img_emoji , pos=center,scale=scale)

    # make emoji motion smooth in case of errors in detecting markers
    elif prev_res!=[]:
        if len(res[2]) > 0:
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, (35, 25, 25), (90, 255,255))
            for marker in res[2]:
                if isMarker(mask,marker):
                    # find center position
                    center=getCenter(marker)
                    
                    scale=(getSize(marker)/80) * 2
                    frame=emojiOverlay(frame , img_emoji , pos=center,scale=scale)
                    break

    cv2.imshow('frame',frame)
    
    """press q to stop webcam recording"""
    k = cv2.waitKey(1) % 256

    if k == ord('q'):
        break
    else:
        """press w to delete emoji overlay"""
        if k == ord('w'):
            imgindex = -1
        """press 0 to 9 or ß or - to add overlayed emoji"""
        for i in range(0,10):
            if k == ord(str(i)):
                imgindex=i
                break;
        if k == ord('ß') or k == ord('-'): # german and english keyboard layout
            imgindex = 10
            

"""When stopping webcam recording, release the capture"""
cap.release()
cv2.destroyAllWindows()