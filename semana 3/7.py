categoria_descuento = input("Ingrese la catergoria del descuento:")
categoria = ["estudiante", "jubilado", "empleado", "otro"]
if categoria_descuento not in categoria:
    print("Categoria no encontrada")
else:
    precio_original = float(input("Ingrese el precio original del producto:"))
    
    if categoria_descuento == "estudiante":
        precio_descuento = precio_original * 0.10
        print(f"El precio final es:{precio_original - precio_descuento}")
        
    elif categoria_descuento == "jubilado":
        precio_descuento = precio_original* 0.15     
        print(f"El precio final es: {precio_original - precio_descuento}")
        
    elif categoria_descuento == "empleado":
        precio_descuento = precio_original * 0.05
        print(f"El precio final es:{precio_original - precio_descuento}")
        
    elif categoria_descuento == "otro":
        precio_descuento = precio_original * 0.00
        print(f"El precio final es:{precio_original - precio_descuento}")