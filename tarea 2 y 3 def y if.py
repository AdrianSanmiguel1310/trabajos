print("====================== BIENVENIDO DE NUEVO =============================",
      "\nContesta esta pregunta.")
print("1.-¿CUANTOS AÑOS TIENES? ",
      "\n  A) ENTRE 1 A 12 AÑOS ",
      "\n  B) ENTRE 12 A 18 AÑOS",
      "\n  C) DE 18 A 30 AÑOS.  ",
      "\n  D) DE 30 A 60 AÑOS   ",
      "\n  E) DE 60 EN ADELANTE ")
def regreso():
    años = input("Escribe una letra de estas.     ")
    if años =="A":
        print("eres menor de edad, edad de niñez.")
        def HP():
            opcion = input("   QUIERES INTERTARLO OTRAVEZ O NO(ESCRIBE ´SI ´NO´): ")
            if opcion == "SI" or opcion == "si" or opcion == "Si" or opcion == "sI":
                regreso()
            elif opcion == "NO" or opcion == "no" or opcion == "No" or opcion == "nO":
                print("BUENO ADIOS")
                exit
            else:
                print("LO SIENTO NO SE REPONDIO A LA PREGUNTA")
                HP()
        HP()
    elif años == "B":
        print("estas en la edad adolecente")
        def HP():
            opcion = input("   QUIERES INTERTARLO OTRAVEZ O NO(ESCRIBE ´SI ´NO´): ")
            if opcion == "SI" or opcion == "si" or opcion == "Si" or opcion == "sI":
                regreso()
            elif opcion == "NO" or opcion == "no" or opcion == "No" or opcion == "nO":
                print("BUENO ADIOS")
                exit
            else:
                print("LO SIENTO NO SE REPONDIO A LA PREGUNTA")
                HP()
        HP()
    elif años == "C":
        print("estas en la edad de la juventud")
        def HP():
            opcion = input("   QUIERES INTERTARLO OTRAVEZ O NO(ESCRIBE ´SI ´NO´): ")
            if opcion == "SI" or opcion == "si" or opcion == "Si" or opcion == "sI":
                regreso()
            elif opcion == "NO" or opcion == "no" or opcion == "No" or opcion == "nO":
                print("BUENO ADIOS")
                exit
            else:
                print("LO SIENTO NO SE REPONDIO A LA PREGUNTA")
                HP()
        HP()
    elif años == "D":
        print("estas en la edad adulta.")
        def HP():
            opcion = input("   QUIERES INTERTARLO OTRAVEZ O NO(ESCRIBE ´SI ´NO´): ")
            if opcion == "SI" or opcion == "si" or opcion == "Si" or opcion == "sI":
                regreso()
            elif opcion == "NO" or opcion == "no" or opcion == "No" or opcion == "nO":
                print("BUENO ADIOS")
                exit
            else:
                print("LO SIENTO NO SE REPONDIO A LA PREGUNTA")
                HP()
        HP()
    elif años == "E":
        print("estas en la edad vieja")
        def HP():
            opcion = input("   QUIERES INTERTARLO OTRAVEZ O NO(ESCRIBE ´SI ´NO´): ")
            if opcion == "SI" or opcion == "si" or opcion == "Si" or opcion == "sI":
                regreso()
            elif opcion == "NO" or opcion == "no" or opcion == "No" or opcion == "nO":
                print("BUENO ADIOS")
                exit
            else:
                print("LO SIENTO NO SE REPONDIO A LA PREGUNTA")
                HP()
        HP()
    else:
        print("lo siento esto que introduciste no es valido.\n")
        regreso()
regreso()

