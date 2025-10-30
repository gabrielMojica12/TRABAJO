class Carro:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.estado_ensamblaje = "Pendiente"
        self.componentes_instalados = []  # [(nombre, material)]

    def set_estado(self, estado):
        self.estado_ensamblaje = estado

    def agregar_componente(self, componente):
                # tupla
        self.componentes_instalados.append((componente.nombre, componente.material))

    def mostrar_info(self):
        print("\n=== Información del carro ===")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.anio}")
        print(f"Estado: {self.estado_ensamblaje}")
        if self.componentes_instalados:
            print("Componentes instalados:")
            for nombre, material in self.componentes_instalados:
                print(f" - Modificación: {nombre}  Material: {material}")
        else:
            print("Aún no se han instalado componentes.")
