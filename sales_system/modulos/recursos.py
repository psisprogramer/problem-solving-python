from datetime import datetime
import os
import json

DATA_PATH = "data"
PRODUCTS_FILE = os.path.join(DATA_PATH, "products.json")
SALES_FILE = os.path.join(DATA_PATH, "sales.json")

def load_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

products = load_json(PRODUCTS_FILE, {})
sales = load_json(SALES_FILE, [])

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
    for id, data in products.items():
        print(f"{id}. {data['name']} - ${data['price']} - Stock: {data['stock']}")

    try:
        product_id = input("\nIngrese el ID del producto: ")

        if product_id not in products:
            print("Producto no válido.")
            return

        quantity = int(input("Ingrese la cantidad: "))

        if quantity <= 0 or quantity > products[product_id]["stock"]:
            print("Cantidad inválida.")
            return

        total = quantity * products[product_id]["price"]
        products[product_id]["stock"] -= quantity

        sale = {
            "date": datetime.now().isoformat(),
            "product_id": product_id,
            "product_name": products[product_id]["name"],
            "quantity": quantity,
            "unit_price": products[product_id]["price"],
            "total": total
        }

        sales.append(sale)

        save_json(PRODUCTS_FILE, products)
        save_json(SALES_FILE, sales)

        print("\nVenta registrada correctamente ✔︎")

    except ValueError:
        print("Entrada inválida.")

    input("\nPresione Enter para continuar...")


