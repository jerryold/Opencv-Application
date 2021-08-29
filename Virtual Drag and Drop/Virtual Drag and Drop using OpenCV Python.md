---
tags: Opencv-Python
---
# Virtual Drag and Drop using OpenCV Python 
* 需安裝套件
    * cvzone
    * opencv
    * numpy
    * mediapipe

* 操作介紹

取得手勢以及長方形方塊之間相對距離
```
def update(self,cursor):

        cx,cy=self.posCenter
        w,h=self.size

        #If the index finger tip is in the rectangle region
        if cx - w // 2 < cursor[0] < cx + w // 2 and \
                cy - h // 2 < cursor[1] < cy + h // 2:  # cursor[0] is x point, cursor[1] is y point
            self.posCenter = cursor
```

Draw Solid(移動實體圖片)
```
         for rect in rectList:
             cx, cy = rect.posCenter
            w, h = rect.size
             cv2.rectangle(img, (cx-w//2,cy-h//2) ,
                           (cx+w//2,cy+h//2), colorR, cv2.FILLED)
            cvzone.cornerRect(img,(cx-w//2,cy-h//2 ,w,h),20, rt=0)
```

Draw Solid(移動實體圖片)
```            
        # Draw Transperency(圖片透明)
        imgNew=np.zeros_like(img,np.uint8)
        for rect in rectList:
            cx, cy = rect.posCenter
            w, h = rect.size
            cv2.rectangle(imgNew, (cx-w//2,cy-h//2) ,
                          (cx+w//2,cy+h//2), colorR, cv2.FILLED)
            cvzone.cornerRect(imgNew,(cx-w//2,cy-h//2 ,w,h),20, rt=0)    
```



![image](https://github.com/jerryold/Opencv-Application/blob/master/Virtual%20Drag%20and%20Drop/Virtual%20Drag.gif)





參考連結
https://www.youtube.com/watch?v=6DxN8G9vB50&ab_channel=Murtaza%27sWorks

