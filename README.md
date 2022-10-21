# 01-Face-Recog-Python
source: https://bit.ly/3ySH8rW
[Video Source](#https://youtu.be/sz25xxF_AVE)

## Notes
An attempt to create a software that recognizes faces from a repository and shows their name.

## Features
- The program identifies a face and includes their name.

## Future plans
- Implement it inside the drone to identify people from far.
- Reduce Lag from Camera
- Add to table, name, time date

# Facial recognition python
[source](#https://www.youtube.com/watch?v=sz25xxF_AVE)

## Facial Recognition

How it works
1. Finding the faces
2. Uses Facial landmarks then warps them to understand the different sides of the face
3. Encoding Faces
    - Measurement of the distance between the eyes the nose of spacial measurements of the facial features.
    - It will generate 128 measurements from the image.
4. Finding the person's name from the encoding

Pycharm

Install dependencies
Project interpreter
Install the following:
Cmake
Dlib (use 19.18.0)
face-recognition
Numpy
Opencv-python
Import all
Import cv2
Import numpy as np
Import face_recognition
