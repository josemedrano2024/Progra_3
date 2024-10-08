class Perro:
    def __init__(self, nombre, raza, edad, peso, color, vacunado, propietario, estado='NO ATENDIDO'):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.color = color
        self.vacunado = vacunado
        self.propietario = propietario
        self.estado = estado
        self.tamano = self.determinar_tamano()

    def determinar_tamano(self):
        if self.peso < 10:
            return "Perro Pequeño"
        else:
            return "Perro Grande"

    def atender(self):
        self.estado = 'ATENDIDO'

    def mostrar_informacion(self):
        return (f'Nombre: {self.nombre}, Raza: {self.raza}, Edad: {self.edad} años, '
                f'Peso: {self.peso} kg, Color: {self.color}, Vacunado: {self.vacunado}, '
                f'Propietario: {self.propietario}, Estado: {self.estado}, Tamaño: {self.tamano}')


def main():
    lista_perros = []

    while True:
        print("\nRegistro de Perros en Veterinaria")
        nombre = input("Ingresa el nombre del perro: ")
        raza = input("Ingresa la raza del perro: ")
        edad = int(input("Ingresa la edad del perro (en años): "))
        peso = float(input("Ingresa el peso del perro (en kg): "))
        color = input("Ingresa el color del perro: ")
        vacunado = input("¿Está vacunado? (Sí/No): ")
        propietario = input("Ingresa el nombre del propietario: ")
        
        # Crear una instancia del perro
        perro = Perro(nombre, raza, edad, peso, color, vacunado, propietario)
        
        # Cambiar el estado a ATENDIDO
        perro.atender()
        
        # Agregar a la lista de perros
        lista_perros.append(perro)
        
        print("\nPerro registrado con éxito!")
        # Mostrar la información del perro
        print(perro.mostrar_informacion())

        # Preguntar si desea registrar otro perro
        continuar = input("\n¿Deseas registrar otro perro? (Sí/No): ")
        if continuar.lower() != 'sí':
            break

    print("\nRegistro finalizado. Gracias por utilizar el sistema.")


if __name__ == "__main__":
    main()
