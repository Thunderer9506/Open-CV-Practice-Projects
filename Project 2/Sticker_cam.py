import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    if not ret:break

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    face_coord = face_cascade.detectMultiScale(gray,1.1,5,minSize=(30,30))
    
    for (x,y,w,h) in face_coord:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),1)

        face_roi = frame[y:y+h,x:x+w]

        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]

        eye_coord = eye_cascade.detectMultiScale(roi_gray,1.09,3)

        for (ex,ey,ew,eh) in eye_coord:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,0),-1)
        
        smile_coord = smile_cascade.detectMultiScale(roi_gray,1.7,40)
        for (sx,sy,sw,sh) in smile_coord:
            cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(0,0,0),-1)

    cv2.imshow("Camera",frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()