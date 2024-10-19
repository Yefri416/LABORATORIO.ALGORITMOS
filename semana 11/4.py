def contar_frecuencia_palabras(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        texto = archivo.read().lower()
        palabras = texto.split()  
        
        frecuencia = {}
        for palabra in palabras:
            palabra = palabra.strip('.,!?;"()[]')
            if palabra:  
                frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

        palabras_comunes = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)[:10]

        print("Las 10 palabras más frecuentes son:")
        for palabra, conteo in palabras_comunes:
            print(f"{palabra}: {conteo}")

nombre_archivo = input("Introduce el nombre del archivo de texto (con .txt): ")
contar_frecuencia_palabras(nombre_archivo)
