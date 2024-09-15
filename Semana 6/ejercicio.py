import random
import string

def generar_contraseña(longitud):
    if longitud < 8:
        raise ValueError("La longitud mínima de la contraseña es de 8 caracteres.")
    
    letras_mayusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    digitos = string.digits
    caracteres_especiales = "!@#$%^&*()-_=+[]{}|;:,.<>?/"
    
    contraseña = [
        random.choice(letras_mayusculas),
        random.choice(letras_minusculas),
        random.choice(digitos),
        random.choice(caracteres_especiales)
    ]
    todos_los_caracteres = letras_mayusculas + letras_minusculas + digitos + caracteres_especiales
    
    while len(contraseña) < longitud:
        contraseña.append(random.choice(todos_los_caracteres))
    random.shuffle(contraseña)
    return ''.join(contraseña)

longitud = int(input("Ingrese el numero de caracteres que quiere para su contraseña: ")) # Puedes cambiar esto a cualquier longitud deseada que sea >= 8
contraseña = generar_contraseña(longitud)
print(contraseña)
