import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    if not ret:break
    
    blurred_frame = cv2.GaussianBlur(frame,(19,19),0)
    hsv_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    COLORS_TO_TRACK = [
        ("blue", np.array([90, 100, 100]), np.array([130, 255, 255]), (255, 0, 0)),
        ("green", np.array([40, 70, 70]), np.array([80, 255, 255]), (0, 255, 0)),
        ("red", np.array([160, 100, 100]), np.array([180, 255, 255]), (0, 0, 255)),
        ("yellow", np.array([17, 58, 50]) , np.array([34, 255, 255]), (255, 255, 0)),
        ("white", np.array([0, 0, 180]), np.array([180, 50, 255]), (255, 255, 255)),
        ("orange", np.array([5, 100, 100]), np.array([25, 255, 255]), (255, 165, 0)),
    ]

    for (color_name, lower_range, upper_range, box_color) in COLORS_TO_TRACK:
        mask = cv2.inRange(hsv_frame, lower_range, upper_range)

        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            c = max(contours, key=cv2.contourArea)
            area = cv2.contourArea(c)

            if area > 500: 
                (x, y, w, h) = cv2.boundingRect(c)

                cv2.rectangle(frame, (x, y), (x+w, y+h), box_color, 2)

                cv2.putText(frame, color_name, (x, y - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, box_color, 2)
                

    cv2.imshow("Multi-Color Tracker", frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()