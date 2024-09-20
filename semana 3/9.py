año = float(input("Ingrese el año: "))
if año // 4:
    print("Este es un año bisieto")
elif (año // 100) or (año // 400):
    print("Este es año bisiesto")
else:
    print("Este año no es bisiesto")