from datetime import datetime
import os


products = {
    1: {"name": "Laptop", "price": 2500, "stock": 5},
    2: {"name": "Mouse", "price": 50, "stock": 20},
    3: {"name": "Keyboard", "price": 120, "stock": 10}
}

def show_products():
    for name, data in products.items():
            print("----- Sales Systems ✔︎ ------------")
            print(f"-Fecha: {datetime.now()} ")
            print(f"--Producto: {name},   --{data['name']}"     )  
            print(f"--Precio: {data['price']} ")
            print(f"--Disponibilidad en tienda: {data['stock']}")
            print("") 
    input("\nPresione Enter para volver al menú principal...")

def find_product():
    name = input("nombre del producto: ").lower()
    encontrado = False

    for id, data in products.items():
        if data["name"].lower() == name:
            print("\n===================================================================")
            print("------------------- Resultado de la búsqueda ☑︎ -------------------")
            print(f"ID: {id}")
            print(f"Producto: {data['name']}")
            print(f"Precio: {data['price']}")
            print(f"Cantidad en stock: {data['stock']}")
            print("===================================================================")
            encontrado = True
            break

    if not encontrado:
        print(f"Producto '{name}' no fue encontrado.")

    input("\n[Presione Enter para continuar...]")

def process_sale(products):
    pass