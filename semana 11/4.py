def buscar_palabra_en_archivo(nombre_archivo, palabra_buscada):
    try:
        with open(nombre_archivo, 'r') as archivo:
            for numero_linea, linea in enumerate(archivo, start=1):
                if palabra_buscada in linea:
                    print(f"Línea {numero_linea}: {linea.strip()}")

    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Solicitar al usuario el nombre del archivo y la palabra a buscar
nombre_archivo = input("Introduce el nombre del archivo de texto (con .txt): ")
palabra_buscada = input("Introduce la palabra que deseas buscar: ")
buscar_palabra_en_archivo(nombre_archivo, palabra_buscada)
