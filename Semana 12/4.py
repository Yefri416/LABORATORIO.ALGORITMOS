productos = [
    {"nombre": "Laptop", "precio": 800},
    {"nombre": "Celular", "precio": 600},
    {"nombre": "Audifonos", "precio": 300},
    {"nombre": "Mouse", "precio": 200}
]

productos.sort(key=lambda x: x["precio"], reverse=True)
print(productos)