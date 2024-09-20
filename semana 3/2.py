lado_1 = int(input("ingrerse la longitud del lado 1:"))
lado_2 = int(input("ingrese la longitud del lado 2:"))
lado_3 = int(input("ingrese la longitud del lado 3:"))
if lado_1 > 0 and lado_2 > 0 and lado_3 > 0 :
    
    if lado_1 == lado_2 == lado_3 :
        print("El triangulo es equilatero.")
    if (lado_1 == lado_2 and lado_1 != lado_3) or \
        (lado_2 == lado_3 and lado_2 != lado_1) or \
        (lado_1== lado_3 and lado_1 != lado_2):
        print("El triangulo es isósceles.")  
    if lado_2 != lado_1 and lado_1 != lado_3 and lado_2 != lado_3:
        print("El triangulo es escaleno.")
else:
    print("Los datos son incorrectos.")