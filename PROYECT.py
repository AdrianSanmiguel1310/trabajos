import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import ttk
import sys 
from PIL import Image, ImageTk
import numpy as np


mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="",
  database = "trabajadores"
)
print(mydb)

ventana=Tk()
ventana.geometry('635x482')
ventana.title('TRABAJADORES')
ventana.configure(background = 'red')

def close_window():
    ventana.destroy()

def LLAMADA_2():
    nmbe_var = StringVar()
    nmbe = Entry(ventana, textvariable=nmbe_var).place(x=440,y=60)
    pusto_var = StringVar()
    pusto = Entry(ventana, textvariable=pusto_var).place(x=440,y=150)
    mail_var = StringVar()
    mail = Entry(ventana, textvariable=mail_var).place(x=440,y=240)

    Label(ventana,text='nombre y apellido').place(x=440, y=40)
    Label(ventana,text='puesto').place(x=440, y=130)
    Label(ventana,text='email').place(x=440, y=220)

    sql="INSERT INTO empleados(nombre, puesto, email) VALUES (%s,%s,%s)"
    datos=(nmbe.execute(), pusto.get(), mail.get() )
    cursor1.execute(sql, datos)
    conexion1.commit()
    conexion1.close()
    
    
def LLAMADA_3():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM `empleados` ")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

    
def LLAMADA_4():
    nmbe_var = tk.StringVar()
    nmbe = ttk.Entry(ventana, textvariable=nmbe_var).place(x=440,y=60)
    pusto_var = tk.StringVar()
    pusto = ttk.Entry(ventana, textvariable=pusto_var).place(x=440,y=150)
    mail_var = tk.StringVar()
    mail = ttk.Entry(ventana, textvariable=mail_var).place(x=440,y=240)

    Label(ventana,text='nombre y apellido').place(x=440, y=40)
    Label(ventana,text='puesto').place(x=440, y=130)
    Label(ventana,text='email').place(x=440, y=220)
    
    mycursor = mydb.cursor()
    sql = "UPDATE empleados SET nombre = '"+nmbe_var.get()+"', puesto = '"+pusto_var.get()+"' WHERE  mail = '"+mail_var.get()+"'"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "se cambio con exito")
    
def LLAMADA_5():
    nmbe_var = tk.StringVar()
    nmbe = ttk.Entry(ventana, textvariable=nmbe_var).place(x=440,y=60)
    
    Label(ventana,text='nombre y apellido').place(x=440, y=40)

    mycursor = mydb.cursor()
    sql = "DELETE FROM empleados WHERE nombre = '"+nmbe_var.get()+"'"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "se elimino el empleado")
        
AGREGAR_EMPLEADO = Button(ventana,text='AGREGAR EMPLEADO',command = LLAMADA_2)
AGREGAR_EMPLEADO.place(x=50, y=120)

MOSTRAR = Button(ventana,text='MOSTRAR EMPLEADOS',command = LLAMADA_3)
MOSTRAR.place(x=50, y=210)

CAMBIOS = Button(ventana,text='HACER CAMBIOS',command = LLAMADA_4)
CAMBIOS.place(x=50, y=300)

BORRAR = Button(ventana,text='BORRAR EMPLEADOS',command = LLAMADA_5)
BORRAR.place(x=50, y=390)

pa_fuera = Button(ventana,text='SALIR',command = close_window )
pa_fuera.place(x=260, y=450)

ventana.mainloop()
