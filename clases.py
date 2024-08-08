import json
import logging
import os
import platform
def limpiar_pantalla():
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

class Producto():
    def __init__(self,nombre,precio,codigoProducto,stock,color,tamaño):
        self.nombre = nombre
        self.precio = precio
        self.codigoProducto = codigoProducto
        self.stock = stock
        self.color = color
        self.tamaño = tamaño
    
    
    def validar_nombre(self, nombre):
        try:
            if isinstance(nombre,str):
                return nombre
            else:
                print("El nombre no es vaido")
             
        except ValueError:
            raise ValueError("Nombre invalido")
    
    def validar_precio(self,precio):
        try:
            if precio < 0:
                print("El precio debe ser mayor o igual a 0")
            return precio
        
        except ValueError:
            raise ValueError("Precio invalido")
    
    def validar_stock(self,stock):
        try:
            if stock < 0 :
                print("El stock debe ser mayor o igual a 0")
            return stock
        
        except ValueError:
            raise ValueError("Stock invalido")
    
    def to_dict(self):
                return {
            "nombre" : self.nombre,
            "precio" : self.precio,
            "codigoProducto" : self.codigoProducto,
            "stock" : self.stock,
            "color" : self.color,
            "tamaño" : self.tamaño
        }
    def __str__(self):
        return f"{self.nombre} {self.precio}"


class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, codigoProducto, stock, color, tamaño, tecnologia):
        super().__init__(nombre, precio, codigoProducto, stock, color, tamaño)
        self.tecnologia = tecnologia
    
    def to_dict(self):
        datosproducto = super().to_dict()
        datosproducto['Tecnologia'] = self.tecnologia
        return datosproducto

    def __str__(self):
        return f"{super().__str__()} - Tecnologia: {self.tecnologia}"
    
class ProductoArtLimpieza(Producto):
    def __init__(self, nombre, precio, codigoProducto, stock, color, tamaño, eficiencia):
        super().__init__(nombre, precio, codigoProducto, stock, color, tamaño)
        self.eficiencia = eficiencia
    
    def to_dict(self):
        datosproducto = super().to_dict()
        datosproducto['Eficiencia'] = self.eficiencia
        return datosproducto

    def __str__(self):
        return f"{super().__str__()} - Eficiencia: {self.eficiencia}"

class GestionProducto:
    def __init__(self,archivo):
        self.archivo = archivo

    def leer_datos(self):
        try:
            with open(self.archivo, 'r') as file:
                datosProducto = json.load(file)
                return datosProducto

        except FileNotFoundError:
            return {}
        except Exception as error:
            raise Exception(f"Error al leer los datos del archivo: {error}")
        
    def guardar_datos(self, datosProducto):
        try:
            with open(self.archivo, 'w') as file:
                json.dump(datosProducto, file, indent=2)
        except IOError as error:
            print(f'Error al intentar guardar los datos de los productos en {self.archivo}: {error}')
        except Exception as error:
            print(f'Error inesperado: {error}')

    def crear_producto(self,producto):
        try:
            datosProductos = self.leer_datos()
            codigoProducto = producto.codigoProducto

            if not str(codigoProducto) in datosProductos.keys():
                datosProductos[str(codigoProducto)] = producto.to_dict()
                self.guardar_datos(datosProductos)
                print("Datos de productos guardados")
                input("Precione ENTER para continuar...")
                
            else:
                print(f'Este codigo de producto ya existe {codigoProducto} ya existe')
        except Exception as ex:
            import logging
            logging.error("Ocurrio un error: {ex}", exc_info=True)
        
    def eliminar_producto(self,codigoProducto):
        try:
            datosProductos = self.leer_datos()
            if str(codigoProducto) in datosProductos.keys():
                del datosProductos[str(codigoProducto)]
                self.guardar_datos(datosProductos)
                print ("Producto Eliminado...")
            else :
                print(f"No se encontro el producto {codigoProducto}")
        except Exception as ex:
            import logging
            logging.error("Ocurrio un error: ", ex, exc_info=True)
        
    def actualizar_producto(self,codigoProducto, dato , datoActualizado):
        try:
            datosProductos = self.leer_datos()
            if str(codigoProducto) in datosProductos:
                datosProductos[str(codigoProducto)][str(dato)] = datoActualizado
                self.guardar_datos(datosProductos)
                print("Producto actualizado")
            else:
                print(f"No se encontró el producto {codigoProducto}")

        except Exception as ex:
            import logging
            logging.error("Ocurrio un error: ", ex, exc_info=True)
    
    def mostrar_producto(self):
        try:
            for producto in self.leer_datos().values():
                if 'Tecnologia' in producto.keys():
                    print(" ")
                    print(f"Nombre: {producto['nombre'].capitalize()} - Stock: {producto['stock']} - Precio: {producto['precio']} - Codigo: {producto['codigoProducto']} Color: {producto['color'].capitalize()} - Tamaño: {producto['tamaño'].capitalize()} - Tecnologia: {producto['Tecnologia'].capitalize()}")
                if 'Eficiencia' in producto.keys():
                    print(" ")
                    print(f"Nombre: {producto['nombre'].capitalize()} - Stock: {producto['stock']} - Precio: {producto['precio']} - Codigo: {producto['codigoProducto']} Color: {producto['color'].capitalize()} - Tamaño: {producto['tamaño'].capitalize()} - Eficiencia: {producto['Eficiencia']}")
        except Exception as ex:
            import logging
            logging.error("Ocurrio un error: ", ex, exc_info=True)
    
    def buscar_producto(self):
        try:    
            limpiar_pantalla()
            print("------------ Buscar Producto ------------")
            print(" ")
            print(" 1- Buscar Producto por codigo")
            print(" 2- Buscar Productos por filtro")
            print(" ")
            print(" Para volver al menu selecciona 0")
            print(" ")
            opcion = input(" Seleccione una opcion: ")
            datosProductos = self.leer_datos()
            if opcion == 0 or opcion == '0':
                from main import reiniciar
                reiniciar()
            elif opcion == 1 or opcion == '1':
                limpiar_pantalla()
                print("---------- Buscando producto por codigo ----------")
                codigoProducto = input("Ingrese el codigo: ")
                                   
                if str(codigoProducto) in datosProductos:
                    datos_producto = datosProductos[str(codigoProducto)]
                    datos_base = f"Nombre: {datos_producto['nombre'].capitalize()} - Stock: {datos_producto['stock']} - Precio: {datos_producto['precio']} - Codigo: {datos_producto['codigoProducto']} - Color: {datos_producto['color'].capitalize()} - Tamaño: {datos_producto['tamaño'].capitalize()}"
                    if 'Tecnologia' in datos_producto:
                        print(" ")
                        print(f"{datos_base} - Tecnologia: {datos_producto['Tecnologia'].capitalize()}")
                        print(" ")
                    elif 'Eficiencia' in datos_producto:
                        print(" ")
                        print(f"{datos_base} - Eficiencia: {datos_producto['Eficiencia']}")
                        print(" ")
                else :
                    print("La opcion seleccionada debe ser un codigo numerio de la lista...")

                input("Presione ENTER para continuar...")
            elif opcion == 2 or opcion == '2': 
                limpiar_pantalla()
                print("---------- Buscando producto por filtro ----------")
                print(" ")
                filtro = input(" Seleccione la clave que desea buscar: ")
                for producto in self.leer_datos().values():
                    if filtro in producto.keys():
                        if 'Tecnologia' in producto.keys():
                            print(" ")                        
                            print(f"Nombre: {producto['nombre'].capitalize()} - Stock: {producto['stock']} - Precio: {producto['precio']} - Codigo: {producto['codigoProducto']} - Color: {producto['color'].capitalize()} - Tamaño: {producto['tamaño'].capitalize()} - Tecnologia: {producto['Tecnologia'].capitalize()}")
                        if 'Eficiencia' in producto.keys():
                            print(" ")
                            print(f"Nombre: {producto['nombre'].capitalize()} - Stock: {producto['stock']} - Precio: {producto['precio']} - Codigo: {producto['codigoProducto']} - Color: {producto['color'].capitalize()} - Tamaño: {producto['tamaño'].capitalize()} - Eficiencia: {producto['Eficiencia']}")
                else:
                    print(" ")
                    print("No se encontro la clave que busca...")
                print(" ")
                input("Presione ENTER para continuar...")
            else:
                print("La opcion seleccionada debe ser un numero de la lista...")
                input("Presiona ENTER para continuar...")

        except ValueError:
                print("Opción inválida. Por favor, ingrese un número.")
        except Exception as e:
                print(f"Ocurrió un error: {e}")