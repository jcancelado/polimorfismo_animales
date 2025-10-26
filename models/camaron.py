from .animal import Animal

class Camaron(Animal):
    def __init__(self, nombre, longitud_mm):
        super().__init__(nombre)
        self.longitud_mm = longitud_mm

    def hacer_sonido(self):
        return f"{self.nombre} hace burbujas bajo el agua."

    def descripcion(self):
        return f"Camarón de {self.longitud_mm} mm"
