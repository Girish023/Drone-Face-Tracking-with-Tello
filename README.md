# Drone Face Tracking with Tello

## Overview

This project implements a face-tracking system using the Tello drone and OpenCV. The drone captures video feed, detects faces in real-time, and adjusts its position to keep the detected face centered in the frame. 

## Features

- Connects to the Tello drone and streams video feed.
- Utilizes OpenCV for face detection.
- Implements a basic PID controller for tracking faces.
- Adjustable parameters for face detection sensitivity and tracking responsiveness.

## Requirements

- Python 3.x
- `djitellopy` library
- `opencv-python` library
- `numpy` library

You can install the required libraries using:

```bash
pip install djitellopy opencv-python numpy
```

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Girish023/Drone-Face-Tracking-with-Tello.git
   cd face_Detection
   ```

2. Ensure you have the Haar Cascade XML file for face detection. You can download it from [OpenCV's GitHub repository](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) and place it in the appropriate directory.

## Usage

1. Initialize the drone:
   ```python
   myDrone = intializeTello()
   ```

2. Start capturing frames and tracking faces:
   ```python
   while True:
       img = telloGetFrame(myDrone)
       img, info = findFace(img)
       pError = trackFace(info, 360, [0.4, 0.4], pError)
       
       cv2.imshow("Drone Camera", img)
       if cv2.waitKey(1) & 0xFF == ord('q'):
           break
   ```

3. Ensure the drone is in an open area to avoid obstacles.

## Parameters

- `fbRange`: Adjustable range for face area detection to control the drone's forward/backward speed.
- `pid`: Coefficients for the PID controller to tune the drone's responsiveness.

## Troubleshooting

- Ensure your drone is fully charged and connected to the same Wi-Fi network.
- Adjust the Haar Cascade path if necessary based on your directory structure.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
