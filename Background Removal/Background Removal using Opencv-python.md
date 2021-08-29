---
tags: Opencv-Python
---
# Background Removal using Opencv-python
* 需安裝套件
    * cvzone
        * cvzone.SelfiSegmentationModule import  SelfiSegmentation
    * opencv
    * numpy
    * mediapipe
    * os
* 介紹
* cap.set(640,480)>>圖片需要統一為(640,480) pixel才能進行背景置換
* function
    * fpsReader=cvzone.FPS():讀取畫面fps
    * segementor.removeBG:更改圖片背,並透過threshold來修正去背效果
    * cvzone.stackImages:將兩個cv2 camera畫面結合


* 參考連結
https://www.youtube.com/watch?v=k7cVPGpnels&ab_channel=Murtaza%27sWorkshop-RoboticsandAI
