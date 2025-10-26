from .animal import Animal

class Aguila(Animal):
    def __init__(self, nombre, envergadura_cm):
        super().__init__(nombre)
        self.envergadura_cm = envergadura_cm

    def hacer_sonido(self):
        return f"{self.nombre} grita: ¡Kyaaaaa!"

    def descripcion(self):
        return f"Águila con envergadura de {self.envergadura_cm} cm"
