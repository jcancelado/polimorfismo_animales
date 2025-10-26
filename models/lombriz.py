from .animal import Animal

class Lombriz(Animal):
    def __init__(self, nombre, longitud_cm):
        super().__init__(nombre)
        self.longitud_cm = longitud_cm

    def hacer_sonido(self):
        return f"{self.nombre} no emite sonidos audibles."

    def descripcion(self):
        return f"Lombriz de {self.longitud_cm} cm"
