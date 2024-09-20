numero_1 = int(input("Ingrese el primer numero:"))
numero_2 = int(input("Ingrese el segundo numero:"))
numero_3 = int(input("Ingrese el tercer numero:"))
if numero_1 > numero_2 > numero_3:
    print("El primer numero es mayor, seguido del segundo")
elif numero_1 > numero_3 > numero_2:
    print("El primer numero es mayor, seguido del tercero")
elif numero_2 > numero_1 > numero_3:
    print("El segundo numero es mayor, seguido del primero")
elif numero_2 > numero_3 > numero_1:
    print("El segundo numero es el mayor, segudio del tercero")
elif numero_3 > numero_2 > numero_1:
    print("El tercer numero es mayor, seguido del segundo")
elif numero_3 > numero_1 > numero_2:
    print("El tercer numero es mayor, seguido po el primero")