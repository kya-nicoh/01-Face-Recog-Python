import cv2
import numpy as np
import face_recognition

imgOne = face_recognition.load_image_file('Images/gabby.jpg')
imgOne = cv2.cvtColor(imgOne, cv2.COLOR_BGR2RGB)
imgTwo = face_recognition.load_image_file('Images/Me.jpg')
imgTwo = cv2.cvtColor(imgTwo, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgOne)[0]
encodeOne = face_recognition.face_encodings(imgOne)[0]
cv2.rectangle(imgOne, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)
faceLocTwo = face_recognition.face_locations(imgTwo)[0]
encodeTwo = face_recognition.face_encodings(imgTwo)[0]
cv2.rectangle(imgTwo, (faceLocTwo[3], faceLocTwo[0]), (faceLocTwo[1], faceLocTwo[2]), (255, 0, 255), 2)

results = face_recognition.compare_faces([encodeOne], encodeTwo)
faceDis = face_recognition.face_distance([encodeOne], encodeTwo)
print(results, faceDis)
cv2.putText(imgOne, f'{results} {round(faceDis[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('First Image', imgTwo)
cv2.imshow('Second Image', imgOne)
cv2.waitKey(0)