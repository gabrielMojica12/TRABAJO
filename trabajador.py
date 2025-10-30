class Trabajador:
    def __init__(self, nombre, id_trabajador, especialidad):
        self.nombre = nombre
        self.id_trabajador = id_trabajador
        self.especialidad = especialidad

    def controlar_maquina(self, maquina):
        print(f"\n {self.nombre} ({self.especialidad}) está controlando la máquina {maquina.tipo}...")
        maquina.activar()
