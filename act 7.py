NUEVANOTA="A"
print("BIENVENIDO \n\n")
def HCL():
    REGISTRO=int(input("INGRESE RESGISTRO: "))
    if REGISTRO>=19 and REGISTRO<=20:
        NUEVANOTA="A"
        print("TU NOTA ES ",NUEVANOTA)
        HCL()
    elif REGISTRO>=16 and REGISTRO<=18:
        NUEVANOTA="B"
        print("TU NOTA ES ",NUEVANOTA)
        HCL()
    elif REGISTRO>=13 and REGISTRO<=15:
        NUEVANOTA="C"
        print("TU NOTA ES ",NUEVANOTA)
        HCL()
    elif REGISTRO>=10 and REGISTRO<=12:
        NUEVANOTA="D"
        print("TU NOTA ES ",NUEVANOTA)
        HCL()
    elif REGISTRO>=1 and REGISTRO<=9:
        NUEVANOTA="E"
        print("TU NOTA ES ",NUEVANOTA)
        HCL()
    else:
        NUEVANOTA="A"
        print("TU NOTA ES ",NUEVANOTA)
        print("FIN DE LA EVALUACION")
HCL()
