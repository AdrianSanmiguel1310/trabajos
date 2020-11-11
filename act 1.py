print("""---------------------- HOLA BIENVENIDO ------------------------\n\n""")
def HOLA():
    print("INTRODUZCA DOS VALORES DISTINOS\n")
    A=int(input("INTRODUCE UN NUMERO : "))
    B=int(input("INTRODUCE OTRO NUMERO: "))
    if A==B:
            print("\n",A," ES IGUAL A ", B,"INGRESA DE NUEVO PORFAVOR")
            HOLA()
    else:
            if A>B:
                print("\n",A," ES EL MAYOR")
                HOLA()
            else:
                print("\n",B," ES EL MAYOR")
                HOLA()
HOLA()
    
            
