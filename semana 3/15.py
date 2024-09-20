usuario = input("Ingresa tu numero de celular de 10 digitos: ")
if len(usuario) == 10: print(f"({usuario[0:3]}){usuario[3:6]} - {usuario[6:10]}")