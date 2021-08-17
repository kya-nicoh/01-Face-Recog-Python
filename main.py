import cv2
import numpy as np
import face_recognition

imgChris = face_recognition.load_image_file('Images/gab and me.jpg')
imgChris = cv2.cvtColor(imgChris, cv2.COLOR_BGR2RGB)
imgRealChris = face_recognition.load_image_file('Images/Chad Thundercock.jpg')
imgRealChris = cv2.cvtColor(imgRealChris, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgChris)[0]
encodeChris = face_recognition.face_encodings(imgChris)[0]
cv2.rectangle(imgChris, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)
faceLocReal = face_recognition.face_locations(imgRealChris)[0]
encodeRealChris = face_recognition.face_encodings(imgRealChris)[0]
cv2.rectangle(imgRealChris, (faceLocReal[3], faceLocReal[0]), (faceLocReal[1], faceLocReal[2]), (255, 0, 255), 2)

results = face_recognition.compare_faces([encodeChris], encodeRealChris)
faceDis = face_recognition.face_distance([encodeChris], encodeRealChris)
print(results, faceDis)
cv2.putText(imgChris, f'{results} {round(faceDis[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('Christopher Lee', imgRealChris)
cv2.imshow('Chad Thundercock', imgChris)
cv2.waitKey(0)