import cv2
import numpy as np

img = cv2.imread('colores.jpg')
hola = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

celeste_bajo = np.array([185,130,0])
celeste_alto = np.array([255,203,81])

rojo_bajo = np.array([18,12,146])
rojo_alto = np.array([199,196,251])

morado_bajo = np.array([18,7,18])
morado_alto = np.array([233,205,233])


mask_celeste = cv2.inRange(hola, celeste_bajo, celeste_alto)
mask_rojo = cv2.inRange(hola, rojo_bajo, rojo_alto)
mask_morado = cv2.inRange(hola, morado_bajo, morado_alto)

mask_union = cv2.bitwise_or(mask_celeste, mask_rojo, mask_morado)

kernel = np.ones((6,6),np.uint8)
mask_union = cv2.morphologyEx(mask_union, cv2.MORPH_CLOSE, kernel)
mask_union = cv2.morphologyEx(mask_union, cv2.MORPH_OPEN, kernel)

cv2.imshow('FOTO ORIGINAL', img)
cv2.imshow('LOS COLORES', mask_union)

cv2.waitKey(0)
cv2.destroyALLWindows()
