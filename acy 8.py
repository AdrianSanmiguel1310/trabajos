print("bienvenido")
def hola():
    A=0
    B=0
    TEMPORAL=0
    A=int(input("INGRESE NUMERO: "))
    B=int(input("INGRESE OTRO NUMERO: "))
    if A>B:
          print("ORDEN =",A,",",B,"\n\n")
          hola()
    else:
          TEMPORAL=B
          B=A
          A=TEMPORAL
          print("ORDEN =",A,",",B,"\n\n")
          hola()
hola()
