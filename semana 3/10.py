variable = float(input("Ingrese la medida que convertira: "))

if variable < 0 :
    print("El numero ingresado es negativo ERROR.")
    
    unidades = ["pies", "pulgadas", "yardas"]
    unidad_convercion = input("Ingrese la unidad de conversion: ")
    if unidad_convercion not in unidades:
        print("Ésta unidad no existe!!") 
    else:
         if unidad_convercion == "pies":
            print( "El resultado es: ", variable * 3.28084 )
         elif unidad_convercion == "pulgadas":
            print("El resultado es: ", variable * 39.7301)
         elif unidad_convercion == "yardas":
            print("El resultado es: ", variable * 1.09361)