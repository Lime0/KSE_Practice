#Window Server Code
#2. server.py

import cv2
import imagezmq

share = imagezmq.ImageHub()

while True:
    rasp,iamge = share.recv_image()
    cv2.imshow(rasp, image)
    if cv2.WaitKey(1) == ord('q'):
        break
    image.send_reply(b'ok')