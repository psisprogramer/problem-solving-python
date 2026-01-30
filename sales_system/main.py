import os
from modulos.recursos import show_products, find_product

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
  
def menu():
    while True:
        limpiar_pantalla()
        print("\n================================================")
        print("-----------------------------------------------")
        print("\nBienvenido a SALES SYSTEM  ©︎ ")
        print("------          Menú principal:          ------")
        print("-1. Mostrar lista de productos.")
        print("-2. Hacer una venta.")
        print("-3. Generar reporte de ventas.")
        print("-0. Salir")
        print("----------------------------------------------") 
        print("===============================================")  
        opcion = input("Ingrese una opción: ")    
        if opcion == "1":
            show_products()
        elif opcion == "2":
            find_product()
        elif opcion == "3":
            #reporte()
             print("algo")
        elif opcion == "0":
            print("Guardando datos...")
            #guardar_datos()
            print("Gracias por usar nuestros servicios.")
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    #cargar_datos() 
    menu()