import cv2
import numpy as np

cap = cv2.VideoCapture(0)

blur_on = False
gray_on = False
canny_on = False
spotlight_on = False

while True:
    ret,frame = cap.read()
    display_frame = frame.copy()

    if not ret:break
    key = cv2.waitKey(1) & 0xFF


    if key == ord('g'):  # 'g' for Grayscale
        gray_on = not gray_on

    if key == ord('b'):  # 'b' for Blur
        blur_on = not blur_on

    if key == ord('c'):  # 'c' for Canny
        canny_on = not canny_on

    if key == ord('s'):  # 's' for Spotlight
        spotlight_on = not spotlight_on

    if blur_on:
        display_frame = cv2.GaussianBlur(display_frame,(21,21),0)
        cv2.putText(display_frame, "Blur: ON", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    if gray_on:
        # Convert to gray, but then convert *back* to 3-channel BGR.
        # This is a trick so you can still draw color text on it later.
        gray = cv2.cvtColor(display_frame, cv2.COLOR_BGR2GRAY)
        display_frame = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        cv2.putText(display_frame, "Gray: ON", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    if canny_on:
        # Canny needs a grayscale image. If gray isn't already on,
        # it's best to make a temp gray version just for this.
        temp_gray = cv2.cvtColor(display_frame, cv2.COLOR_BGR2GRAY)
        canny_edges = cv2.Canny(temp_gray, 50, 150)
        # Canny is also 1-channel, so convert it back to 3-channel BGR.
        display_frame = cv2.cvtColor(canny_edges, cv2.COLOR_GRAY2BGR)
        cv2.putText(display_frame, "Canny: ON", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    if spotlight_on:
        mask = np.zeros_like(display_frame)
        h,w,_ = display_frame.shape
        center_x = w//2
        center_y = h//2
        cv2.circle(mask, (center_x, center_y), 150, (255, 255, 255), -1)
        display_frame = cv2.bitwise_and(display_frame, mask)
        cv2.putText(display_frame, "Spotlight: ON", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow("Filer App",display_frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()