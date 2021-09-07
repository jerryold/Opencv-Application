---
tags: Opencv-Python
---
# Virtual Zoom in and out
* 需安裝套件
    * cvzone
    * opencv
    * numpy
    * mediapipe

* 操作介紹


取得兩手之間距離,並求出放大和放小的value值
```
 if startDistance is None:
                length,info,img =detector.findDistance(lmList1[8],lmList2[8],img)
                print(length)
                startDistance=length

            
            length, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
            scale = int((length-startDistance)//2) #negatvue value:zoom in,positive value:zoom out
            cx,cy=info[4:]
            print(scale)
```

計算圖片和手勢Zoom in & Zoom out距離
```

    try:
        h1, w1, _=img1.shape
        newH,newW=((h1+scale)//2)*2,((w1+scale)//2)*2
        img1=cv2.resize(img1,(newW,newH))

        img[cy-newH//2:cy+newH//2,cx-newW//2:cx+newW//2]=img1 #Image location    
```








https://user-images.githubusercontent.com/12774427/132369609-43cab0e4-4f4c-4586-9d65-74dd025a090a.mp4




參考連結
https://www.youtube.com/watch?v=VPaFV3QBsEw&ab_channel=Murtaza%27sWorkshop-RoboticsandAI

