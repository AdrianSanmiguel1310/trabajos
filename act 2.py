print("        BIENVENIDO USUARIO PORFAVOR INTRODUCE TRES NO. DISTINTOS")
def RETURN():
    A=float(input("\n\n  INTRODUCE UN NUMERO: "))
    B=float(input("  OTRO NUMERO: "))
    C=float(input("  Y OTRO: "))
    if A>B and A>C:
        print("\n    ",A," ES EL MAYOR")
        RETURN()
    elif B>A and B>C:
        print("\n    ",B," ES EL MAYOR")
        RETURN()
    else:
        print("\n    ",C," ES EL MAYOR")
        RETURN()
RETURN()
