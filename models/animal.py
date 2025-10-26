class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return f"{self.nombre} hace un sonido genérico."

    def descripcion(self):
        return f"Soy un animal llamado {self.nombre}."
