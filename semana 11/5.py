def copiadora_archivos(archivo_origen, archivo_destino):
    with open(archivo_origen, 'r', encoding='utf-8') as origen:
        with open(archivo_destino, 'r', encoding='utf-8') as destino:
            for linea in origen:
                destino.write(linea)
                print(f"El contenido de {archivo_origen} se copió en {archivo_destino}.")
                
archivo_origen = input("Ingrese el nombre del archivo origen: ")
archivo_destino = input("Ingrese el nombre del archivo destino: ")
copiadora_archivos(archivo_origen, archivo_destino)
