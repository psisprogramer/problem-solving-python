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

def process_sale():
        print("\n================ SISTEMA DE VENTAS =================")

        for id, data in products.items():
            print(f"{id}. {data['name']} - Precio: {data['price']} - Stock: {data['stock']}")

        try:
            product_id = int(input("\nIngrese el ID del producto: "))

            if product_id not in products:
                print("Producto no válido.")
                input("\nPresione Enter para continuar...")
                return

            cantidad = int(input("Ingrese la cantidad a vender: "))

            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0.")
                input("\nPresione Enter para continuar...")
                return

            if cantidad > products[product_id]["stock"]:
                print("No hay suficiente stock disponible.")
                input("\nPresione Enter para continuar...")
                return

            total = cantidad * products[product_id]["price"]
            products[product_id]["stock"] -= cantidad

            print("\n===================================================")
            print("--------------- Venta realizada ✔︎ ----------------")
            print(f"Fecha: {datetime.now()}")
            print(f"Producto: {products[product_id]['name']}")
            print(f"Cantidad vendida: {cantidad}")
            print(f"Total a pagar: ${total}")
            print("===================================================")

        except ValueError:
            print("Entrada inválida. Debe ingresar números.")

        input("\nPresione Enter para volver al menú principal...")
