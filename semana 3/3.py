suma = 0
contador = 0
nota1 = input("Introduce la primera nota o (sacar promedio) para terminar: ")
if nota1.lower() != 'sacar promedio':
    suma += float(nota1)
    contador += 1
    
    nota2 = input("Introduce la segunda nota o (sacar promedio) para terminar: ")
    if nota2.lower() != 'sacar promedio':
        suma += float(nota2)
        contador += 1

        nota3 = input("Introduce la tercera nota o (sacar promedio) para terminar: ")
        if nota3.lower() != 'sacar promedio':
            suma += float(nota3)
            contador += 1

if contador > 0:
    promedio = suma / contador
    print(f"El promedio de las notas es: {promedio}")
else:
    print("No se ingresaron notas.")
