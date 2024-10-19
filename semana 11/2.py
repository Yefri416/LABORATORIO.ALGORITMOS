import csv

def procesar_csv(nombre_archivo):
    try:
        with open(nombre_archivo, newline='') as archivo:
            lector = csv.reader(archivo)
            datos = []
            for fila in lector:
                for valor in fila:
                    datos.append(float(valor))
                    
            if datos:
                media = sum(datos) / len(datos)
                maximo = max(datos)
                minimo = min(datos)
                
                print(f"Media: {media:.2f}")
                print(f"Valor máximo: {maximo:.2f}")
                print(f"Valor mínimo: {minimo:.2f}")
            else:
                print("No se encontraron datos numéricos en el archivo.")
                
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encontró.")
        
nombre_archivo = input("Introduce el nombre del archivo CSV (con .csv): ")
procesar_csv(nombre_archivo)