import cv2
import numpy as np

img = cv2.imread('AQUA.jpg')
hola = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
aqua_bajo = np.array([50,43,1])
aqua_alto = np.array([255,252,232])
mask = cv2.inRange(hola, aqua_bajo, aqua_alto)
cv2.imshow('FOTO ORIGINAL', img)
cv2.imshow('ENCONTRE AQUA EN', mask)

cv2.waitKey(0)
cv2.destroyALLWindows()
