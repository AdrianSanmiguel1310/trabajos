print("BIENVENIDO")
J=2
S=0
N=float(input("INGRESE NUMERO: "))
while J==N%2:
        if 0==N/J:
            S+=1
            J+=1
            break
        else:
            continue
if S== N%2:
    print(N,"ES PRIMO ")
else:
    print(N, "NO ES PRIMO ")
