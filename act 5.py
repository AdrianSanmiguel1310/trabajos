print("BIENVENIDO COMO ESTAS")
print("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
def vegetta():
    R=0
    H=0
    R=float(input("\n\nINRODUCE EL NO. DE EL RADIO: "))
    H=float(input("INTRODUC LA ALTURA(QUE SEA NUMERO): "))
    VOL=(3.1416)*pow(R,2)*H
    AREA=2*(3.1416)*R*H
    print("\nEL AREA ES: ",AREA,"\nEL VOLUMEN ES: ", VOL)
    def manzana():
        respuesta = input("\n\n¿QUIERES INTERTARLO DE NUEVO?: ")
        if respuesta == "si" or respuesta == "SI" or respuesta == "Si" or respuesta == "sI":
            vegetta()
        elif respuesta == "no" or respuesta == "NO" or respuesta == "No" or respuesta == "nO":
            exit
        else:
            print("\n\nNO VALIDO NO ES RESPUESTA A LA PREGUNTA")
            manzana()
    manzana()    
vegetta()
