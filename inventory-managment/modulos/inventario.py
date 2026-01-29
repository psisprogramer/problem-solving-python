import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INVENTARIO_PATH = os.path.join(BASE_DIR, "inventario.json")
REGISTROS_PATH = os.path.join(BASE_DIR, "registros.json")


import json
from datetime import datetime

# Variables globales (deben importarse en main.py)


InventarioGeneral = {}
Registros = []

#Funcion para cargar datos en JSON
def cargar_datos():
    global InventarioGeneral, Registros  # Para modificar variables globales
    try:
        with open(INVENTARIO_PATH, "r") as inv_file:
            InventarioGeneral = json.load(inv_file)  # Cargar inventario
        with open("registros.json", "r") as reg_file:
            Registros = json.load(reg_file)  # Cargar registros
        print("Datos cargados correctamente.")
    except FileNotFoundError:
        print("No se encontraron archivos previos. Iniciando con inventario vacío.")
# Función para guardar datos en JSON
def guardar_datos():
    with open("inventario.json", "w") as inv_file:
        json.dump(InventarioGeneral, inv_file, indent=4)
    with open("registros.json", "w") as reg_file:
        json.dump(Registros, reg_file, indent=4)
#Función para crear productos
def crear_productos(): 
    while True:#Ciclo para que el usuario pueda seguir ingresando productos antes de volver al menú principal 
        code = input("Ingrese el código del producto: ")
        if code not in InventarioGeneral:#Validación del código ingresado en el diccionario del inventario
            nombre = input("Ingrese el nombre: ")
            proveedor = input("Ingrese el proveedor: ")
            InventarioGeneral[code] = {
                'name': nombre, 
                'prove': proveedor, 
                'bodegas': {'Norte': 0, 'Centro': 0, 'Oriente': 0}#Definición del diccionario de bodegas
            }
            guardar_datos()
            print("\n=================================================================")
            print("-----------------------------------------------------------------")
            print("----------------------Registro exitoso ✔︎-------------------------")
            print(f"-Fecha: {datetime.now()} ------------------------------")
            print(f"--Producto: {nombre}            --Proveedor: {proveedor} ")
            print(f"Código del producto: {code}")
            print("----------------------------------------------------------------")
            print("") #Salidas
            print("=================================================================")
        else:
            print("Código ya registrado") 
        switch = input("¿Desea ingresar otro producto? (si/no): ").lower()
        if switch != 'si':
            break
#Función para ingresar productos
def ingresar_productos():
    try: #validación para ingresar enteros en la variable cantidad
        code = input("Código del producto: ") #entrada
        if code in InventarioGeneral: #Valida si el codigo ingresado esta en el diccionario Inventario general
            bodega = input("Bodega (Norte/Centro/Oriente): ").capitalize() #Entrada - Solicita en que bodega desea realizar el ingreso
            if bodega in InventarioGeneral[code]['bodegas']:
                cantidad = int(input("Cantidad: "))
                if cantidad < 0: # Validación para asegurarse de que la cantidad no sea negativa
                    print("La cantidad no puede ser negativa. Intente de nuevo.")
                    return
                    
                InventarioGeneral[code]['bodegas'][bodega] += cantidad
                Registros.append({ 
                    'codigo': code, 'tipo': 'EN', 'cantidad': cantidad, 
                    'bodega': bodega, 'descripcion': 'Ingreso', 
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
        
    except ValueError : 
        print("Ingrese una cantidad valida")  
#Función para sacar productos
def sacar_productos():
    code = input("Código del producto: ")
    if code in InventarioGeneral:
        bodega = input("Bodega (Norte/Centro/Oriente): ").capitalize()#Entrada - Solicita en que bodega desea realizar el ingreso
        if bodega in InventarioGeneral[code]['bodegas']:
            try:
                cantidad = int(input("Cantidad: "))
            except ValueError:
                print("Ingrese una cantidad válida")
            return
            if cantidad <= 0: # Validación para asegurarse de que la cantidad no sea negativa
                    print("La cantidad debe ser mayor a cero. Intente de nuevo.")
                    return
            if InventarioGeneral[code]['bodegas'][bodega] >= cantidad:
                InventarioGeneral[code]['bodegas'][bodega] -= cantidad
                Registros.append({  #Se hace el ingreso de ese diccionario en la lista de registros
                    'codigo': code, 'tipo': 'SA', 'cantidad': cantidad, 
                    'bodega': bodega, 'descripcion': 'Salida', 
                    'fecha': datetime.now().isoformat()
                })
                guardar_datos()
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
#Función para buscar productos
def buscar_productos():
    code = input("Código del producto: ") 
    if code in InventarioGeneral:
        print("\n===================================================================")
        print("------------------- Resultado de la busqueda ☑︎ --------------------")
        print(f"Producto: {InventarioGeneral[code]['name']}")
        print("Cantidad en bodegas: ")
        for bodega, cantidad in InventarioGeneral[code]['bodegas'].items():
            print(f"{bodega}: {cantidad}")
            print("===================================================================")
    else:
        print(f"Producto con código {code} no fue encontrado.")