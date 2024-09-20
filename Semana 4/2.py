usuario = int(input("Ingrese un numero entero positivo: "))
if usuario <= 0:
        print("Este numero no es positivo.")
else:
     secuencia = [usuario]
     while usuario != 1:
          if usuario % 2 == 0:
             print(usuario // 2)
          else:
             print((usuario * 3) + 1)
          secuencia.append(usuario)
     print("Secuencia collats es:", secuencia)
