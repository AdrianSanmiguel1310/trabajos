import cv2
import numpy as np

img = cv2.imread('colores.jpg')
hola = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
aqua_bajo = np.array([81,56,0])
aqua_alto = np.array([255,247,225])
mask = cv2.inRange(hola, aqua_bajo, aqua_alto)
cv2.imshow('FOTO ORIGINAL', img)
cv2.imshow('ENCONTRE AQUA EN', mask)

cv2.waitKey(0)
cv2.destroyALLWindows()
