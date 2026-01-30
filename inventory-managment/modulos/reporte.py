from modulos.inventario import Registros, InventarioGeneral, INVENTARIO_PATH, REGISTROS_PATH
from datetime import datetime
import json

def mostrar_historial():
    if not Registros:
        print("No hay historial disponible o archivos no encontrados.")
        return
        
    print("\n=== Historial de Movimientos ===")
    for reg in Registros:
        tipo = "Entrada" if reg["tipo"] == "EN" else "Salida"
        # Formateamos la fecha para que sea más legible
        fecha_formateada = datetime.fromisoformat(reg['fecha']).strftime('%Y-%m-%d %H:%M:%S')
        
        print(f"""
Fecha: {fecha_formateada}
Código: {reg['codigo']} 
Tipo: {tipo}
Cantidad: {reg['cantidad']}
Bodega: {reg['bodega']}
Descripción: {reg['descripcion']}
{'-'*40}""")

def reporte():
    if not InventarioGeneral:
        print("No hay datos de inventario disponibles.")
        return
        
    total_productos = 0
    print("\n=== Reporte de Inventario ===")
    
    for codigo, producto in InventarioGeneral.items():
        print(f"\nProducto: {producto['name']} (Código: {codigo})")
        print(f"Proveedor: {producto['prove']}")
        total_bodega = 0
        
        for bodega, cantidad in producto['bodegas'].items():
            print(f"{bodega}: {cantidad}")
            total_bodega += cantidad
        
        print(f"Total del producto: {total_bodega}")
        total_productos += total_bodega
    
    print(f"\nTotal general en inventario: {total_productos}")
    
    