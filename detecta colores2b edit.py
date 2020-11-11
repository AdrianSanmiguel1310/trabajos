
#
#
#Detecta objetos verdes, elimina el ruido y busca su centro
 
import cv2
import numpy as np
 
#Iniciamos la camara
captura = cv2.VideoCapture(0)
 
while(1):
     
    #Capturamos una imagen y la convertimos de RGB -> HSV
    _, imagen = captura.read()
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
 
    #Establecemos el rango de colores que vamos a detectar
    #En este caso de verde oscuro a verde-azulado claro
    celeste_bajos = np.array([54,46,12], dtype=np.uint8)
    celeste_altos = np.array([242,232,191], dtype=np.uint8)

    morado_bajos = np.array([58,27,58], dtype=np.uint8)
    morado_altos = np.array([221,179,221], dtype=np.uint8)

    rojo_bajos = np.array([175,100,20], dtype=np.uint8)
    rojo_altos = np.array([179, 255, 255], dtype=np.uint8)
 
    #Crear una mascara con solo los pixeles dentro del rango de verdes
    mask = cv2.inRange(hsv, celeste_bajos, celeste_altos)
    mask_2 = cv2.inRange(hsv, morado_bajos, morado_altos)
    mask_3 = cv2.inRange(hsv, rojo_bajos, rojo_altos)

    kernel = np.ones((6,6),np.uint8)
 
    #Encontrar el area de los objetos que detecta la camara
    mam = cv2.add(mask, mask_2, mask_3)
    ma = cv2.morphologyEx(mam, cv2.MORPH_CLOSE, kernel)
    ma = cv2.morphologyEx(mam, cv2.MORPH_OPEN, kernel)
    moments= cv2.moments(mam)
    area = moments['m00']
 
    #Descomentar para ver el area por pantalla
    #print area
    if(area > 2000000):
         
        #Buscamos el centro x, y del objeto
        x = int(moments['m10']/moments['m00'])
        y = int(moments['m01']/moments['m00'])
         
        #Mostramos sus coordenadas por pantalla
        print ("x = ", x)
        print ("y = ", y)
 
        #Dibujamos una marca en el centro del objeto
        cv2.rectangle(imagen, (x, y), (x+2, y+2),(0,0,255), 2)
     
     
    #Mostramos la imagen original con la marca del centro y
    #la mascara
    cv2.imshow('mask', mam)
    cv2.imshow('Camara', imagen)
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
 
cv2.destroyAllWindows()
