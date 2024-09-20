import random
opciones = ["piedra", "papel", "tijera"]
usuario = input("elije piedra, papel o tijera:").lower()
if usuario not in opciones:
    print("opcion invalida")
else:
    computadora = random.choice(opciones)
    print(f"La computadora elijio:{computadora}")
    if usuario == computadora:
        print("¡Empate!")
    elif (usuario == "piedra" and computadora == "tijera")or \
        (usuario == "papel" and computadora == "piedra")or \
        (usuario == "tijera" and computadora == "papel"):
        print("¡ganaste!")
    else:
        print("¡Perdiste!")