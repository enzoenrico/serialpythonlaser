import cv2
import facerecon


while True:
    print(facerecon.coord_face)
    if cv2.waitKey('q'):
        break