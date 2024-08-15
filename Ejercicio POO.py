class Prenda:
    def __init__(self, nombre, categoria, talla, color, precio_compra, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.talla = talla
        self.color = color
        self.precio_compra = precio_compra
        self.cantidad = cantidad

    def mostrar_informacion(self):
        return (f'Nombre: {self.nombre}, Categoría: {self.categoria}, '
                f'Talla: {self.talla}, Color: {self.color}, '
                f'Precio de Compra: {self.precio_compra:.2f}, '
                f'Cantidad en Stock: {self.cantidad}')


class Inventario:
    def __init__(self):
        self.prendas = []

    def agregar_prenda(self):
        print("\nRegistro de una nueva prenda")
        nombre = input("Ingresa el nombre de la prenda: ")
        categoria = input("Ingresa la categoría de la prenda: ")
        talla = input("Ingresa la talla de la prenda: ")
        color = input("Ingresa el color de la prenda: ")
        precio_compra = float(input("Ingresa el precio de compra de la prenda: "))
        cantidad = int(input("Ingresa la cantidad disponible en stock: "))
        
        prenda = Prenda(nombre, categoria, talla, color, precio_compra, cantidad)
        self.prendas.append(prenda)
        print("Prenda registrada con éxito.")

    def consultar_prendas(self):
        if not self.prendas:
            print("No hay prendas registradas en el inventario.")
            return
        print("\nLista de prendas registradas:")
        for prenda in self.prendas:
            print(prenda.mostrar_informacion())


def main():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Inventario de Ropa ---")
        print("1. Agregar prenda")
        print("2. Consultar prendas")
        print("3. Salir")
        opcion = input("Elige una opción (1-3): ")

        if opcion == '1':
            inventario.agregar_prenda()
        elif opcion == '2':
            inventario.consultar_prendas()
        elif opcion == '3':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elige una opción válida.")


if __name__ == "__main__":
    main()

#Este programa proporciona una solución para la gestión del inventario de una tienda de ropa. 
# Permite a los empleados llevar un control adecuado de las prendas disponibles, 
# facilitando la adición de nuevos artículos y la consulta de la información existente. De esta manera, 
# se mejora la gestión de los recursos de la tienda y se optimiza el servicio al cliente, 
# ya que los empleados pueden acceder rápidamente a los detalles de las prendas en stock.