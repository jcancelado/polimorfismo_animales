from .animal import Animal

class Guacamayo(Animal):
    def __init__(self, nombre, color_plumaje):
        super().__init__(nombre)
        self.color_plumaje = color_plumaje

    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Hola! ¡Hola!"

    def descripcion(self):
        return f"Guacamayo de plumaje {self.color_plumaje}"
