palabra1 = input("Introduce la primera palabra: ")
palabra2 = input("Introduce la segunda palabra: ")

if palabra1 < palabra2:
    print(f"{palabra1} va primero y {palabra2} va segundo.")
elif palabra1 > palabra2:
    print(f"{palabra2} va primero y {palabra1} va segundo")
else:
    print("Las palabras son iguales.")