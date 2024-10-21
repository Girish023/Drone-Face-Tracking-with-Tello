from utillity import *
import cv2
w, h=360,240
pid=[0.4,0.4,0]
pError=0
startCounter=1  #o for flight and 1 for no flight 
myDrone = intializeTello()

while True:
    if startCounter==0:
        myDrone.takeoff()
        startCounter=1

    #step 1
    imgd = telloGetFrame(myDrone,w,h)
    img = findFace(imgd)
    info = findFace(imgd)
    pError=trackFace(myDrone,info,pid,pError)
    print(info[0][1])

    cv2.imshow("MyResult", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        myDrone.land()
        break