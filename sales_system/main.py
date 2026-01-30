import os
from modulos.recursos import show_products, find_product, process_sale

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
        print("-2. Buscar producto.")
        print("-3. Hacer una venta.")
        print("-4. Generar reporte de ventas.")
        print("-0. Salir")
        print("----------------------------------------------") 
        print("===============================================")  
        opcion = input("Ingrese una opción: ")    
        if opcion == "1":
            show_products()
        elif opcion == "2":
            find_product()
        elif opcion == "3":
            process_sale()
        elif opcion == "4":
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