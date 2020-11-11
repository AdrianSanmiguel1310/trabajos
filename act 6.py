print("""                  BIENVENIDO

       ++++++++++
        ++++++++
         ++++++ """)
def adrian():
    N=0
    N=int(input("introduce un numero (que sea entero): "))
    B=N%2
    if B==0:
        print(N ," ES PAR.")
        def manzana():
            respuesta = input("\n\n¿QUIERES INTERTARLO DE NUEVO?: ")
            if respuesta == "si" or respuesta == "SI" or respuesta == "Si" or respuesta == "sI":
                adrian()
            elif respuesta == "no" or respuesta == "NO" or respuesta == "No" or respuesta == "nO":
                exit
            else:
                print("\n\nNO VALIDO NO ES RESPUESTA A LA PREGUNTA")
                manzana()
        manzana()    
    else:
        print(N," NO ES PAR")
        def manzana():
            respuesta = input("\n\n¿QUIERES INTERTARLO DE NUEVO?: ")
            if respuesta == "si" or respuesta == "SI" or respuesta == "Si" or respuesta == "sI":
                adrian()
            elif respuesta == "no" or respuesta == "NO" or respuesta == "No" or respuesta == "nO":
                exit
            else:
                print("\n\nNO VALIDO NO ES RESPUESTA A LA PREGUNTA")
                manzana()
        manzana()
adrian()
     
