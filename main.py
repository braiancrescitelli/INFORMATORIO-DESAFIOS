import os
import platform
import json
from clases import (
    ProductoArtLimpieza,
    ProductoElectronico,
    GestionProducto
)
def limpiar_pantalla():
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

def verificar_opcion(opcion):
    if opcion == 0 or opcion == '0':
        return opcion
    elif isinstance(opcion, int):
        return opcion
    else:
        print("La opcion seleccionada debe ser un numero de la lista...")

reiniciar_bucle = False
def reiniciar():
    global reiniciar_bucle
    reiniciar_bucle = True

def mostrar_menu():
    print ("----------Menu de Gestion de Productos----------")
    print(" ")
    print(" 1- Agregar Producto ")
    print(" 2- Eliminar Producto")
    print(" 3- Actualizar Producto")
    print(" 4- Mostrar todos los Productos")
    print(" 5- Buscar Producto")
    print(" ")
    print(" Para salir del menu presione 0")
    print(" ")

def agregar_producto(gestion):
    try:
        limpiar_pantalla()
        print("------------- Agregando Producto -------------")
        print(" ")
        print(" 1- Agregar Producto Electronico")
        print(" 2- Agregar Producto de Limpieza")
        print(" ")
        print(" Para volver al menu selecciona 0")

        opcion2 = input(" Seleccione una opcion: ")
        verificar_opcion(opcion2)
        if opcion2 == 0 or opcion2  == '0':
            reiniciar()
        elif opcion2 == 1  or opcion2 == '1':
            limpiar_pantalla()
            print(" ----------- Agregando Producto Electronico ----------")
            print(" ")
            nombre=str(input("Ingrese el nombre del Producto: "))
            precio=int(input("Ingrese el precio del Producto: "))
            codigoProducto=int(input("Ingrese el codigo del Producto: "))
            stock=int(input("Ingrese el stock del Producto: "))
            color=str(input("Ingrese el color del Producto: "))
            tamaño=str(input("Ingrese el tamaño del Producto: "))
            tecnologia =str(input("Ingrese el tipo de Tecnologia del Producto: "))
            producto = ProductoElectronico(nombre, precio, codigoProducto, stock, color, tamaño, tecnologia)
        elif opcion2 == 2 or opcion2 == '2':
            limpiar_pantalla()
            print(" ----------- Agregando Producto de Limpieza ----------")
            print(" ")
            nombre=str(input("Ingrese el nombre del Producto: "))
            precio=int(input("Ingrese el precio del Producto: "))
            codigoProducto=int(input("Ingrese el codigo del Producto: "))
            stock=int(input("Ingrese el stock del Producto: "))
            color=str(input("Ingrese el color del Producto: "))
            tamaño=str(input("Ingrese el tamaño del Producto: "))
            eficiencia =str(input("Ingrese el tipo de Eficiencia del Producto: "))
            producto = ProductoArtLimpieza(nombre, precio, codigoProducto, stock, color, tamaño, eficiencia)   
        gestion.crear_producto(producto)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

def eliminar_producto_por_codigo(gestion):
    try:
        limpiar_pantalla()
        print(" ----------- Eliminando Producto -----------")
        print(" ")
        print("  Para volver al menu selecciona 0")
        print(" ")
        codigoProducto = input(" Ingrese el codigo del Producto que desea eliminar: ")
        if codigoProducto == 0 or codigoProducto == '0':
            reiniciar()
        else:
            gestion.eliminar_producto(codigoProducto)
            input(" Presione ENTER para continuar")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    
def actualizar_producto_por_codigo(gestion):
    try:
        limpiar_pantalla()
        print("------------ Actualizando Producto ------------")
        print(" ")
        print("  Para volver al menu selecciona 0")
        print(" ")
        codigoProducto = int(input("Ingrese el codigo del Producto: "))
        if codigoProducto == 0 or codigoProducto == '0':
            reiniciar()
        else:
            dato = str(input("Ingrese el dato que quiere actualizar: "))
            datoActualizado = str(input("Ingrese el dato actualizado: "))
            gestion.actualizar_producto(codigoProducto,dato,datoActualizado)
            input("Presione ENTER para continuar...")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    
def mostrar_productos(gestion):
    try:
        limpiar_pantalla()
        print("----------- Productos en venta -----------")
        gestion.mostrar_producto()
        input("Presione ENTER para continuar")
    except ValueError as e:
        print(f"Error : {e}")

def buscar_producto(gestion):
    gestion.buscar_producto()


if __name__ == "__main__":
    archivo_productos= 'productos.json'
    gestionProducto = GestionProducto(archivo_productos)
    
    while True:
        reiniciar_bucle = False
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("Seleccione la opcion: ")
        verificar_opcion(opcion)
        if opcion == 0 or opcion == '0':
            break 
        elif reiniciar_bucle:
            print("Volviendo al menu...")
            reiniciar_bucle = False
            continue

        elif opcion == 1 or opcion == '1':
            agregar_producto(gestionProducto)
        elif opcion == 2 or opcion == '2':
            eliminar_producto_por_codigo(gestionProducto)
        elif opcion == 3 or opcion == '3':
            actualizar_producto_por_codigo(gestionProducto)
        elif opcion == 4 or opcion == '4':
            mostrar_productos(gestionProducto)
        elif opcion == 5 or opcion == '5':
            buscar_producto(gestionProducto)
        else:
            input("Presione ENTER para continuar...")