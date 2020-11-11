import cv2
import numpy as np

img = cv2.imread('MARRON.jpg')
hola = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
aqua_bajo = np.array([5,17,39 ])
aqua_alto = np.array([221, 232, 251])
mask = cv2.inRange(hola, aqua_bajo, aqua_alto)
cv2.imshow('FOTO ORIGINAL', img)
cv2.imshow('ENCONTRE AQUA EN', mask)

cv2.waitKey(0)
cv2.destroyALLWindows()
