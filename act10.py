print("HOLA BIENVENIDO")
HE=0
HS=0
PAGO=0
HE=float(input("INTRODUCE HORA DE ENTRADA: "))
HS=float(input("INTRODUCE HORA DE SALIDA: "))
HORA_ESTADIA = HS - HE
FRACCION = HORA_ESTADIA - HORA_ESTADIA
if HORA_ESTADIA>=1:
    if FRACCION>=1:
        HORA_ESTADIA = HORA_ESTADIA + 1
        HORAS_RESTANTES = HORA_ESTADIA - 1
        PAGO = 1000 + (HORAS_RESTANTES * 600)
        print("PAGA ",PAGO)
        exit
    else:
        HORAS_RESTANTES = HORA_ESTADIA - 1
        PAGO = 1000 + (HORAS_RESTANTES * 600)
        print("PAGA ",PAGO)
        exit
else:
    PAGO = 1000
    print("PAGA ",PAGO)
