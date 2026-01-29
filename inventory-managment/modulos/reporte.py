from modulos.inventario import Registros, InventarioGeneral
from datetime import datetime
import json

#Función para mostrar el historial
def mostrar_historial():
    try: 
        with open('registros.json', 'r') as f: 
            registros = json.load(f)
        
        print("\n=== Historial de Movimientos ===")
        for reg in registros:
            tipo = "Entrada" if reg["tipo"] == "EN" else "Salida"
            print(f"""
Fecha: {datetime.fromisoformat(reg['fecha']).strftime('%Y-%m-%d %H:%M:%S')}
Código: {reg['codigo']} 
Tipo: {tipo}
Cantidad: {reg['cantidad']}
Bodega: {reg['bodega']}
Descripción: {reg['descripcion']}
{'-'*40}""") #Para poner lineas
    except FileNotFoundError:
        print("No hay historial disponible")

def reporte():
    try:
        with open('inventario.json', 'r') as f:
            inventario = json.load(f)
        
        total_productos = 0
        print("\n=== Reporte de Inventario ===")
        
        for codigo, producto in inventario.items():
            print(f"\nProducto: {producto['name']} (Código: {codigo})")
            print(f"Proveedor: {producto['prove']}")
            total_bodega = 0
            
            for bodega, cantidad in producto['bodegas'].items():
                print(f"{bodega}: {cantidad}")
                total_bodega += cantidad
            
            print(f"Total del producto: {total_bodega}")
            total_productos += total_bodega
        
        print(f"\nTotal general en inventario: {total_productos}")
    except FileNotFoundError:
        print("No hay datos de inventario disponibles")




