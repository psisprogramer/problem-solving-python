import json
import os
from datetime import datetime

DATA_PATH = "data"
SALES_FILE = os.path.join(DATA_PATH, "sales.json")


def load_sales():
    if not os.path.exists(SALES_FILE):
        return []
    with open(SALES_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def sales_report():
    sales = load_sales()

    if not sales:
        print("\nNo hay ventas registradas.")
        input("\nPresione Enter para volver...")
        return

    total_general = 0

    print("\n================= REPORTE DE VENTAS =================")
    for sale in sales:
        print(f"Fecha: {sale['date']}")
        print(f"Producto: {sale['product_name']}")
        print(f"Cantidad: {sale['quantity']}")
        print(f"Total: ${sale['total']}")
        print("---------------------------------------------------")
        total_general += sale["total"]

    print(f"\nTOTAL GENERAL DE VENTAS: ${total_general}")
    print("====================================================")

    input("\nPresione Enter para volver al menú...")
