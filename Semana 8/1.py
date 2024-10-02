def convertir_temperatura(a):
    tipo_temperatura = input("ingrese el tipo de temperatura,(c para celcius) y (f para Fahrenheit): ")
    if tipo_temperatura == "c":
        x = a*1.8 + 32
        return (f"Su temperatura en Fahrenheit es {x}.")
    elif tipo_temperatura == "f":
        y = ((a - 32) / 1.8)
        return (f"Su temperatura en Celcius es {y}.")

print(convertir_temperatura(int(input("ingrese su temperatura: "))))