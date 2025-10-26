import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    if not ret:break

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    face_coord = face_cascade.detectMultiScale(gray,1.1,5,minSize=(30,30))
    
    for (x,y,w,h) in face_coord:
        """
            to blur everything outside of the face
        """
        # blur = cv2.medianBlur(frame,21)
        # cv2.rectangle(blur,(x,y),(x+w,y+h),(255,0,0),1)
        # face_roi = frame[y:y+h,x:x+w]
        # blur[y:y+h,x:x+w] = face_roi
        """
            to blur the face
        """
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),1)
        face_roi = frame[y:y+h,x:x+w]
        blurred_face = cv2.medianBlur(face_roi,21)
        frame[y:y+h,x:x+w] = blurred_face

    cv2.imshow("Camera",frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()