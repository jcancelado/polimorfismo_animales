from models.guacamayo import Guacamayo
from models.camaleon import Camaleon
from models.camaron import Camaron
from models.lombriz import Lombriz
from models.aguila import Aguila

class AnimalViewModel:
    def __init__(self):
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def listar_animales(self):
        print("\n=== Lista de animales ===")
        for a in self.animales:
            print(f"{a.nombre}: {a.descripcion()}")

    def sonidos(self):
        print("\n=== Sonidos de los animales ===")
        for a in self.animales:
            print(a.hacer_sonido())

    def cargar_datos_demo(self):
        #Cargar algunos animales de ejemplo"""
        self.agregar_animal(Guacamayo("Paco", "rojo-azul"))
        self.agregar_animal(Camaleon("Camilo", "verde"))
        self.agregar_animal(Camaron("Cami", 25))
        self.agregar_animal(Lombriz("Lomi", 4.5))
        self.agregar_animal(Aguila("Ari", 180))
