numero = int(input("Escribe un numero entero positivo:")) 
if numero <= 0:
    print("El numero ingresado es incorrecto.")
else:
    for x in range(1,10):
        print(f"{x} x {numero} = {x * numero}")