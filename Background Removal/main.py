import cv2
import cvzone
from cvzone.SelfiSegmentationModule import  SelfiSegmentation
import os

cap=cv2.VideoCapture(0)
cap.set(3,640) #hegiht
cap.set(4,480) #width
cap.set(cv2.CAP_PROP_FPS,60)
segementor=SelfiSegmentation()
fpsReader=cvzone.FPS()
imgBg=cv2.imread("Images/1.jpg") #Background setting

listImg=os.listdir("Images")
print(listImg)
imgList=[]
for imgPath in listImg:
    img=cv2.imread(f'Images/{imgPath}') #Read different image
    imgList.append(img)
print(len(imgList))
indexImg=0



while True:
    success, img=cap.read()
    imgOut=segementor.removeBG(img,imgList[indexImg],threshold=0.75) #threshold can control the cut range

    imgStacked=cvzone.stackImages([img,imgOut],2,1) #combine the two screen
    _,imgStacked=fpsReader.update(imgStacked,color=(0,0,255))
    print(indexImg)
    cv2.imshow("Image" , imgStacked)
    key = cv2.waitKey(1)
    if key == ord('d'):
        if indexImg>0:
            indexImg -= 1
    elif key == ord('a'):
        if indexImg < len(imgList)-1:
            indexImg += 1
    elif key == ord('q'):
        break
