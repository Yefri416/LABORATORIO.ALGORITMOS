def contar_vocales(palabra):
    vocales = 'aeiouAEIOU'
    return sum(1 for letra in palabra if letra in vocales)

def insertion_sort_por_vocales(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1

        vocales_clave = contar_vocales(clave)
        
        while j >= 0 and contar_vocales(lista[j]) < vocales_clave:
            lista[j + 1] = lista[j]
            j -= 1
        
        lista[j + 1] = clave


palabras = ["hola", "mundo", "python", "programación", "program", "py"]
insertion_sort_por_vocales(palabras)
print(palabras)