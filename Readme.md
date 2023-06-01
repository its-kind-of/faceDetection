# Real-Time Face Detection with OpenCV and Mediapipe
This is a Python program that utilizes OpenCV and Mediapipe libraries to perform real-time face detection from a video feed or webcam. It detects faces in the input frames, draws bounding boxes around them, and displays the frames with the detected faces.

# Requirements
To run this program, you need to have the following dependencies installed:
```
Python 3.x
OpenCV
Mediapipe
```
You can install OpenCV and Mediapipe using the following command:

```pip install opencv-python mediapipe```

# Usage
1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt and navigate to the directory where the code is saved.
3. Run the following command to start the program:

```python face_detection.py
```
4. The program will use your default webcam as the video source by default. If you want to use a different video source, you can modify the code accordingly (e.g., change 0 to the video file path in cap = cv2.VideoCapture(0)).
Output
The program will display a window showing the live video feed with bounding boxes around the detected faces. It also shows the frames per second (FPS) in the top-left corner of the window.

# Customization
You can customize the behavior of the program by modifying the FaceDetector class and its methods in the face_detection.py file. For example, you can change the minimum detection confidence, adjust the drawing style of the bounding boxes, or add additional annotations to the detected faces.

# References
* OpenCV: https://opencv.org/
* Mediapipe: https://mediapipe.dev/
Feel free to explore and modify the code as per your requirements. Enjoy face detection in real-time!

_Note: Make sure to have a working webcam or provide a valid video file path to test the program._