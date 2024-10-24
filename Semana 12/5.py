def ordenar_por_ultima_letra(palabras):
    return sorted(palabras, key=lambda palabra: palabra[-1])

lista_palabras = ["manzana", "fresa", "plátano", "kiwi"]
palabras_ordenadas = ordenar_por_ultima_letra(lista_palabras)

print(palabras_ordenadas)