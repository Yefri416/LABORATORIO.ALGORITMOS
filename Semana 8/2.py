def calculadora():
    try:
        numero_1 = int(input("Ingrese el primer numero: "))
        numero_2 = int(input("Ingrese el segundo numero: "))
        operacion = input("Ingrese la operacion a realizar: ")
        if operacion == "suma":
            adicion = numero_1 + numero_2
            print(f"la respuesta es {adicion}")
        elif operacion == "resta":
            sustraccion = numero_1 - numero_2
            print(f"la respuesta es {sustraccion}")
        elif operacion == "multiplicacion":
            producto = numero_1 * numero_2
            print (f"la respuesta es {sustraccion}")
        try:
            if operacion == "division":
                if numero_1 != 0 or numero_2 != 0:
                    cociente = numero_1 / numero_2
                    print(f"la respuesta es {cociente}")
        except ZeroDivisionError: 
            print("ERROR, ocurrio un error en la division por cero.")
    except ValueError:
        print("ERROR, hay un error de entrada.")
    finally: 
        print("Siempre se ejecuta.")
calculadora()