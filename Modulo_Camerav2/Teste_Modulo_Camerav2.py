from picamera import PiCamera
from time import sleep

camera = PiCamera()


"O código a seguir é usado para definir a resolução para o máximo e tirar uma foto"

camera.resolution = (2592, 1944)
camera.framerate = 15
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/max.jpg')
camera.stop_preview()
