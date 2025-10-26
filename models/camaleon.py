from .animal import Animal

class Camaleon(Animal):
    def __init__(self, nombre, color_actual):
        super().__init__(nombre)
        self.color_actual = color_actual

    def hacer_sonido(self):
        return f"{self.nombre} se queda en silencio…"

    def descripcion(self):
        return f"Camaleón de color {self.color_actual}"
