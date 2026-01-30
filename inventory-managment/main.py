from modulos.inventario import (
    crear_productos, ingresar_productos, 
    sacar_productos, buscar_productos,
    guardar_datos, cargar_datos
)
from modulos.reporte import mostrar_historial, reporte

# Función de menú
def menu():
    while True:
        print("\n================================================")
        print("-----------------------------------------------")
        print("\nBienvenido a ACME'S GESTIÓN DE INVENTARIOS ©︎ ")
        print("------          Menú principal:          ------")
        print("-1. Registrar productos.")
        print("-2. Ingresar productos.")
        print("-3. Retirar productos del inventario.")
        print("-4. Buscar productos en inventario.")
        print("-5. Historial.")
        print("-6. Reporte.")
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
            buscar_productos()
        elif opcion == "5":
            mostrar_historial()
        elif opcion == "6":
            reporte()
        elif opcion == "0":
            print("Guardando datos...")
            guardar_datos() # <--- IMPORTANTE: Asegura la persistencia al salir
            print("Gracias por usar nuestros servicios.")
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    cargar_datos() 
    menu()