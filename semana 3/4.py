usuario = input ("ingrese la operacion que va a realizar:")
operaciones = ["suma", "resta", "multiplicacion", "division"]

if usuario not in operaciones:
    print("operacion invalida!!")
else:
    numero_1 = float(input("ingrese el primer numero:"))
    numero_2 = float(input("ingrese el segundo numero:"))
    
    if usuario == "suma" :
        print(numero_1 + numero_2)
    if usuario == "resta":
        if numero_2 < numero_1:
            print(numero_1 - numero_2)
        elif numero_1 < numero_2:
            print(numero_2 - numero_1)
    if usuario == "multiplicacion":
        print(numero_1 * numero_2)
    if usuario == "division":
        if numero_1 > numero_2:
            print(numero_1 // numero_2)
        elif numero_2 > numero_1:
            print(numero_2 // numero_1)