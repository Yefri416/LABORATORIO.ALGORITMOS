def procesador_de_texto():
    with open(nombre_archivo, 'a') as archivo:
        texto = input("Ingrese su texto: ")
        archivo.write(texto + '\n')
        print(f"Texto agregado al archivo {nombre_archivo} con éxito.")

nombre_archivo = input("Introduce el nombre del archivo en modo .txt: ")
procesador_de_texto()