print("""              BIENVENIDO
ESTE RPOGRAMA DETERMINARA LA HIPOTENUSA DE DOS CATETOS: """)
def JJ():
    CATA=0
    CATB=0
    print("\n\nVALOR DE LOS CATETOS",CATA,CATB)
    CATA=float(input("introduce cateto A: "))
    CATB=float(input("introduce cateto b: "))
    SUMA = CATA + CATB
    import math
    HIP = math.sqrt(SUMA)
    print("\n\n EL VALOR DE LA HIPOTENUSA ES: ",HIP)
    def vv():
        respuesta=input("\n\n    ¿QUIRES INTERTARLO OTRAVEZ? ")
        if respuesta == "no" or respuesta == "No" or respuesta == "nO" or respuesta =="NO":
            exit
        elif respuesta == "SI" or respuesta == "sI" or respuesta == "Si" or respuesta =="si":
            JJ()
        else:
            print("\n\neso no es una respuesta: ")
            vv()
    vv()
JJ()
