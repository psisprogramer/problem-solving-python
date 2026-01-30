import os
from modulos.inventario import (
    crear_productos, ingresar_productos, 
    sacar_productos, buscar_productos,
    guardar_datos, cargar_datos, eliminar_producto
)
from modulos.reporte import mostrar_historial, reporte

def limpiar_pantalla():
    # 'cls' para Windows, 'clear' para Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')
  
def menu():
    while True:
        limpiar_pantalla()
        print("\n================================================")
        print("-----------------------------------------------")
        print("\nBienvenido a ACME'S GESTIÓN DE INVENTARIOS ©︎ ")
        print("------          Menú principal:          ------")
        print("-1. Registrar productos.")
        print("-2. Ingresar productos.")
        print("-3. Retirar productos del inventario.")
        print("-4. Eliminar producto.")
        print("-5. Buscar productos en inventario.")
        print("-6. Historial.")
        print("-7. Reporte.")
        print("-0. Salir")
        print("----------------------------------------------") 
        print("===============================================")  
        
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            crear_productos()
        elif opcion == "2":
            ingresar_productos()
        elif opcion == "3":
            sacar_productos()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            buscar_productos()
        elif opcion == "6":
            mostrar_historial()
        elif opcion == "7":
            reporte()
        elif opcion == "0":
            print("Guardando datos...")
            guardar_datos()
            print("Gracias por usar nuestros servicios.")
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    cargar_datos() 
    menu()