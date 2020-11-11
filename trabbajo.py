import cv2
import image
from PIL import Image
from tkinter import *
import numpy as np
ABRIR_WINDOW=Tk()
ABRIR_WINDOW.geometry('636x351')
ABRIR_WINDOW.title('TOMADOR DE FOTOGRAFIA')
jojo= PhotoImage(file ='konohha.png')
fondo=Label(ABRIR_WINDOW,image=jojo).place(x=0,y=0)
def close_window():
    ABRIR_WINDOW.destroy()
def TOMAR_FOTOGRAFIA():
    camara = cv2.VideoCapture(0)
    leido,frame = camara.read()
    if leido == True:
        cv2.imwrite('fotografia.png',frame)
        labilo=Label(ABRIR_WINDOW,text='LA FOTOGRAFIA SE HIZO CON EXITO')
        labilo.place(x=240,y=170)
        Label(ABRIR_WINDOW,text='abriendo imagen').place(x=240,y=120)
        imagen = cv2.imread('fotografia.png',1)
        prro = cv2.imshow('imagen Abierta',imagen)
    PREGUNTA=Label(ABRIR_WINDOW,text='¿QUIERES INTERTARLO DE NUEVO?')
    PREGUNTA.place(x=320,y=30)
    
    monitor = Label(ABRIR_WINDOW)
    monitor.pack()
    opcion = IntVar()
    DECISION=Radiobutton(ABRIR_WINDOW,text='SI',variable= opcion, command = TOMAR_FOTOGRAFIA)
    DECISION.place(x=360,y=70)
    bton=Radiobutton(ABRIR_WINDOW,text='NO',variable = opcion, command= quit)
    bton.place(x=400,y=70)
    camara.release()
bton=Button(ABRIR_WINDOW,text='TOMAR FOTOGRAFIA',command=TOMAR_FOTOGRAFIA)
bton.place(x=40,y=30)
bton_2=Button(ABRIR_WINDOW,text='SALIR DEL PROGRAMA',command= close_window)
bton_2.place(x=40,y=100)


ABRIR_WINDOW.mainloop()
