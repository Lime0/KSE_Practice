
#Raspberry Pi3
#1. client.py code
import socket
import time
form imutils.video import VideoStream
import imagezmq

share = imageazmq.imageSender(connect_to='tcp: ServerIP:5555' )
rasp = socket.gethostname()

cam = VidoemStream(usePiCamera =True).start()
time.sleep(2.0)

while True:
    image = cam.read()
    share.send_image(rasp,image)