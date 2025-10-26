# Importamos usando el nombre del paquete raíz (asumiendo que ejecutas desde la carpeta "proyecto")
from vm.animal_viewmodel import AnimalViewModel

def main():
    vm = AnimalViewModel()
    vm.cargar_datos_demo()
    vm.listar_animales()
    vm.sonidos()

if __name__ == "__main__":
    main()
