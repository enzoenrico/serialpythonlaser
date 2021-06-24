import cv2
import sys
import time

import serial
import serialprint


eye_cascade_path = "C:/Users/Microsoft/AppData/Local/Programs/Python/Python39/lib/site-packages/cv2/data/haarcascade_eye.xml"
face_cascade_path = "C:/Users/Microsoft/AppData/Local/Programs/Python/Python39/lib/site-packages/cv2/data/haarcascade_frontalface_default.xml"

face_cascade = cv2.CascadeClassifier((face_cascade_path))
eye_cascade = cv2.CascadeClassifier((eye_cascade_path))

font = cv2.FONT_HERSHEY_COMPLEX_SMALL

video = cv2.VideoCapture(0)

# serialprint.startup()

print('[+] Programa iniciado...')

while True:
    ret, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )

    eyes = eye_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )

    for(x, y, w, h) in faces:
        global coord_face

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        coord_face = x, y

        # cv2.putText(video, coord_face, (50, 50), font,
        #             1, (255, 255, 0), 2, cv2.LINE_AA)

        print(f"[~]Coord rosto: {coord_face}")

    for(x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        coord_eye = x, y


#pfv como q escreve a coordenada no rosto mano pqp
        # cv2.putText(video, coord_eye, (20, 20), font,
        #             1, (255, 0, 255), 1, cv2.LINE_AA)

        coord_eye_ard = f"X{x} Y{y}"

        serialprint.write_coords(coord_eye_ard)

        print(f"[~]Coord olho: {coord_eye}")
        # print(coord_eye_ard)


    # time.sleep(.25)

    cv2.imshow('[~]Aperte "q" para sair', frame)

    if(cv2.waitKey(1) == ord('q')):
        break

video.relase()
cv2.destroyAllWindows()
