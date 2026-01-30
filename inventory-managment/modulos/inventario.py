import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INVENTARIO_PATH = os.path.join(BASE_DIR, "inventario.json")
REGISTROS_PATH = os.path.join(BASE_DIR, "registros.json")


import json
from datetime import datetime

InventarioGeneral = {}
Registros = [] 

def cargar_datos():
    global InventarioGeneral, Registros
    try:
        with open(INVENTARIO_PATH, "r") as inv_file:
            InventarioGeneral = json.load(inv_file)
        with open(REGISTROS_PATH, "r") as reg_file:
            Registros = json.load(reg_file)
        print("✔ Datos cargados correctamente.")
    except (FileNotFoundError, json.JSONDecodeError):
        InventarioGeneral = {}
        Registros = []
        print("Aviso: No se encontraron datos previos, iniciando vacío.")

def guardar_datos():
    # ¡Importante! Usar las rutas absolutas aquí también
    with open(INVENTARIO_PATH, "w") as inv_file:
        json.dump(InventarioGeneral, inv_file, indent=4)
    with open(REGISTROS_PATH, "w") as reg_file:
        json.dump(Registros, reg_file, indent=4)

def crear_productos(): 
    while True:
        code = input("Ingrese el código del producto: ")
        if code not in InventarioGeneral:
            nombre = input("Ingrese el nombre: ")
            proveedor = input("Ingrese el proveedor: ")
            InventarioGeneral[code] = {
                'name': nombre, 
                'prove': proveedor, 
                'bodegas': {'Norte': 0, 'Centro': 0, 'Oriente': 0}
            }
            guardar_datos()
            print("\n=================================================================")
            print("-----------------------------------------------------------------")
            print("----------------------Registro exitoso ✔︎-------------------------")
            print(f"-Fecha: {datetime.now()} ------------------------------")
            print(f"--Producto: {nombre}            --Proveedor: {proveedor} ")
            print(f"Código del producto: {code}")
            print("----------------------------------------------------------------")
            print("") 
            print("=================================================================")
        else:
            print("Código ya registrado") 
        switch = input("¿Desea ingresar otro producto? (si/no): ").lower()
        if switch != 'si':
            break
    input("\nPresione Enter para volver al menú principal...")

def ingresar_productos():
    code = input("Código del producto: ") # Entrada
    
    if code in InventarioGeneral: # Valida si el código existe
        bodega = input("Bodega (Norte/Centro/Oriente): ").capitalize() 
        
        if bodega in InventarioGeneral[code]['bodegas']:
            try:
                # Solo envolvemos la conversión de tipo en el try para mayor claridad
                cantidad = int(input("Cantidad: "))
                
                if cantidad <= 0: # Validación: no tiene sentido ingresar 0 o negativos
                    print("La cantidad debe ser mayor a cero. Intente de nuevo.")
                    return
                    
            except ValueError:
                print("Ingrese una cantidad válida (número entero).")
                return

            # Si pasa las validaciones, procedemos con la lógica
            InventarioGeneral[code]['bodegas'][bodega] += cantidad
            
            Registros.append({ 
                'codigo': code, 
                'tipo': 'EN', 
                'cantidad': cantidad, 
                'bodega': bodega, 
                'descripcion': 'Ingreso', 
                'fecha': datetime.now().isoformat()
            })
            
            guardar_datos()
            
            print("\n===================================================================")
            print("-----------------------------------------------------------------")
            print("---------              ⬇︎ ENTRADA(EN)⬇︎                 -----------")
            print(f"---------------------Registro exitoso----------------------------")
            print(f"-Fecha: {datetime.now()} ------------------------------")
            print(f"--Bodega: {bodega}            --Código: {code} ")
            print(f"Cantidad ingresada: {cantidad}")  
            print("------------------------------------------------------------------")
            print("===================================================================")
        else:
            print("Bodega no válida.")
    else:
        print("Producto no encontrado.")
    input("\n[Presione Enter para continuar...]")

def sacar_productos():
    code = input("Código del producto: ")
    if code in InventarioGeneral:
        bodega = input("Bodega (Norte/Centro/Oriente): ").capitalize()
        if bodega in InventarioGeneral[code]['bodegas']:
            try:
                cantidad = int(input("Cantidad: "))
                # La validación de cantidad debe ocurrir inmediatamente después de la conversión
                if cantidad <= 0:
                    print("La cantidad debe ser mayor a cero. Intente de nuevo.")
                    return
            except ValueError:
                print("Ingrese una cantidad válida")
                return

            # Verificación de stock disponible
            if InventarioGeneral[code]['bodegas'][bodega] >= cantidad:
                InventarioGeneral[code]['bodegas'][bodega] -= cantidad
                
                # Registro del movimiento
                Registros.append({
                    'codigo': code, 
                    'tipo': 'SA', 
                    'cantidad': cantidad, 
                    'bodega': bodega, 
                    'descripcion': 'Salida', 
                    'fecha': datetime.now().isoformat()
                })
                
                guardar_datos()
                
                # Tus prints originales
                print("\n===================================================================")
                print("-----------------------------------------------------------------")
                print("---------              ⬆ SALIDA(SA) ⬆︎                 -----------")
                print(f"---------------------Registro exitoso----------------------------")
                print(f"-Fecha: {datetime.now()} ------------------------------")
                print(f"--Bodega: {bodega}            --Código: {code} ")
                print(f"Cantidad retirada: {cantidad}")  
                print("------------------------------------------------------------------")
                print("===================================================================")
            else:
                print("Stock insuficiente.")
        else:
            print("Bodega no válida.")
    else:
        print(f"Producto con código {code} no fue encontrado.")
    input("\n[Presione Enter para continuar...]")

def buscar_productos():
    code = input("Código del producto: ") 
    if code in InventarioGeneral:
        print("\n===================================================================")
        print("------------------- Resultado de la busqueda ☑︎ --------------------")
        print(f"Producto: {InventarioGeneral[code]['name']}")
        print("Cantidad en bodegas: ")
        for bodega, cantidad in InventarioGeneral[code]['bodegas'].items():
            print(f"  {bodega}: {cantidad}")  
        print("===================================================================")
    else:
        print(f"Producto con código {code} no fue encontrado.")
    input("\n[Presione Enter para continuar...]")

def eliminar_producto():
    code = input("Ingrese el código del producto que desea eliminar: ")
    
    if code in InventarioGeneral:
        nombre = InventarioGeneral[code]['name']
        
        # Confirmación de seguridad
        confirmar = input(f"¿Está seguro de eliminar '{nombre}'? (si/no): ").lower()
        if confirmar == 'si':
            # Eliminamos el producto del diccionario
            del InventarioGeneral[code]
            
            # Registramos en el historial
            Registros.append({
                'codigo': code, 
                'tipo': 'ELIM', 
                'cantidad': 0, 
                'bodega': 'N/A', 
                'descripcion': f'Producto {nombre} eliminado del sistema', 
                'fecha': datetime.now().isoformat()
            })
            
            guardar_datos()
            print(f"✔ El producto '{nombre}' ha sido eliminado correctamente.")
    else:
        print("⚠ Error: Producto no encontrado.")
    input("\n[Presione Enter para continuar...]")