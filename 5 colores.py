import cv2
import numpy as np

img = cv2.imread('tabladecolores.png')
hola = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

marron_bajo = np.array([14,0,60])
marron_alto = np.array([52,0,230])

azul_bajo = np.array([100,10,150])
azul_alto = np.array([130,255,255])

naranja_bajo = np.array([0,107,225])
naranja_alto = np.array([47,146,255])

rosa_bajo = np.array([224,6,255])
rosa_alto = np.array([249,206,255])

cafe_bajo = np.array([26,51,74])
cafe_alto = np.array([162,193,223])


mask_marron = cv2.inRange(hola, marron_bajo, marron_alto)
mask_azul = cv2.inRange(hola, azul_bajo, azul_alto)
mask_naranja = cv2.inRange(hola, naranja_bajo, naranja_alto)
mask_rosa = cv2.inRange(hola, rosa_bajo, rosa_alto)
mask_cafe = cv2.inRange(hola, cafe_bajo, cafe_alto)

mask_union = cv2.bitwise_or(mask_marron,mask_azul)
union_2 = cv2.bitwise_or(mask_union,mask_naranja)
unt = cv2.bitwise_or(union_2,mask_rosa)
total = cv2.bitwise_or(unt,mask_cafe)

cv2.imshow('FOTO ORIGINAL', img)
cv2.imshow('LOS COLORES', total)

cv2.waitKey(0)
cv2.destroyALLWindows()
