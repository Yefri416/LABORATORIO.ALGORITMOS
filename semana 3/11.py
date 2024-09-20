peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

IMC = peso / (altura**2)
print(f"Su indice de masa corporal es: {IMC}")
if IMC > 18.5 and IMC < 24.9:
    print("Su peso es normal.")
elif IMC > 25.0 and IMC < 29.9:
    print("Usted está en sobrepeso.")
elif IMC > 30.0:
    print("Usted esta en obesidad.") 