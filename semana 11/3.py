def bucar_palabra(nombre_archivo, palabra_buscar):
    with open(nombre_archivo, 'r') as archivo:
        for numero_linea, linea in enumerate(archivo, start=1):
                if palabra_buscar in linea:
                    print(f"linea {numero_linea} : {linea.strip()}")
                    
                    
nombre_archivo = input("Ingrese el nombre de su archivo.txt: ")
palabra_buscar = input("Ingrese la palabra que quiere buscar: ")
bucar_palabra(nombre_archivo,palabra_buscar)