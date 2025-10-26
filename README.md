# OpenCV Python Mini-Projects

This repository contains four foundational OpenCV projects built in a single day, designed to practice core computer vision concepts. The projects move from basic object detection and ROI manipulation to interactive filters and color-based tracking.

## Core Libraries Used
* **`opencv-python`**: The primary library for all computer vision tasks.
* **`numpy`**: Used for array manipulation, especially for creating masks and defining color ranges.

## How to Run
1.  Ensure you have Python, `opencv-python`, and `numpy` installed.
2.  Download the required Haar Cascade `.xml` files (`haarcascade_frontalface_default.xml`, `haarcascade_eye_tree_eyeglasses.xml`, `haarcascade_smile.xml`) and place them in the same directory as your scripts.
3.  Run any project file using `python <filename>.py`.
4.  Press **'q'** to quit any of the real-time video feeds.

---

## Project 1: Real-time Face Anonymizer

This script detects faces from a live webcam feed and applies a blur or pixelation effect to anonymize them in real-time.

**Features:**
* Live face detection from a webcam.
* Applies a `cv2.medianBlur()` to the detected face region.
* Demonstrates the fundamental concept of Region of Interest (ROI) slicing.

**Key Functions Learned:**
* `cv2.CascadeClassifier()`: To load the pre-trained Haar cascade model for face detection.
* `detectMultiScale()`: To find the coordinates `(x, y, w, h)` of all faces.
* **ROI Slicing**: Using NumPy array slicing (`frame[y:y+h, x:x+w]`) to select *only* the face rectangle.
* Pasting the blurred ROI back onto the main frame.

---

## Project 2: Face/Eye/Smile Sticker Cam

This project extends Project 1 by performing **nested detection**. It first finds a face, then searches *only within* the face's ROI to find eyes and a smile, overlaying simple rectangles to simulate "stickers."

**Features:**
* Loads three separate Haar cascade models (face, eye, smile).
* Optimized detection by searching for eyes/smiles within the smaller face ROI, not the full frame.
* Draws filled rectangles (`-1`) over detected features.
* Includes parameter tuning (`scaleFactor`, `minNeighbors`) to reduce false positives.

**Key Functions Learned:**
* **Nested Detection**: Running `detectMultiScale()` on an ROI (`roi_gray`) rather than the full `gray` frame.
* Managing multiple cascade classifiers.
* Understanding how drawing on an ROI (`roi_color`) directly modifies the original `frame`.

---

## Project 3: Real-time Webcam Filter App

An interactive webcam app that allows the user to toggle various filters on and off using keyboard commands.

**Features:**
* **Keyboard Toggles**:
    * `g`: Toggle Grayscale filter.
    * `b`: Toggle Gaussian Blur filter.
    * `c`: Toggle Canny Edge Detection.
    * `s`: Toggle a "Spotlight" effect.
* **HUD**: Uses `cv2.putText()` to display the status of active filters on-screen.

**Key Functions Learned:**
* **`cv2.waitKey() & 0xFF`**: To capture specific keyboard presses (`ord('g')`).
* **State Management**: Using boolean variables (`blur_on = not blur_on`) to track which filters are active.
* **Bitwise Masking**: Creating a black mask with `np.zeros_like()`, drawing a white circle on it, and using `cv2.bitwise_and()` to create the spotlight effect.
* Converting 1-channel images (Grayscale, Canny) back to 3-channel BGR (`cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)`) for consistent display.

---

## Project 4: Multi-Color Tracker

This script detects and tracks multiple objects based on their color in real-time. It processes each color independently and draws a labeled, color-coded bounding box around the largest detected object of that color.

**Features:**
* Tracks multiple colors (blue, green, red, etc.) simultaneously.
* Uses a scalable design: new colors can be added simply by defining their HSV range in a list.
* Filters out small, noisy detections by checking `cv2.contourArea()`.
* Labels each tracked object with its color name using `cv2.putText()`.

**Key Functions Learned:**
* **`cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)`**: Converting from BGR to HSV color space, which is more reliable for color detection.
* **`cv2.inRange()`**: Creating a binary mask based on a lower and upper HSV color boundary.
* **`cv2.findContours()`**: To find all the distinct "blobs" in the binary mask.
* `max(contours, key=cv2.contourArea)`: To find the largest contour in a list.
* `cv2.boundingRect()`: To get the `(x, y, w, h)` for drawing a rectangle around a contour.
