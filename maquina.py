class Maquina:
    def __init__(self, id_maquina, tipo):
        self.id_maquina = id_maquina
        self.tipo = tipo
        self.activa = False

    def activar(self):
        self.activa = True
        print(f" Máquina {self.tipo} activada y lista para trabajar.")

    def instalar_objeto(self, carro, objeto):
        if not self.activa:
            print(" Error: la máquina no está activa.")
            return

        print(f"\n Instalando {objeto.nombre} ({objeto.material}) en el carro...")
        objeto.instalar()
        carro.agregar_componente(objeto)
        carro.set_estado("Ensamblado parcialmente")
        print(" Instalación completada correctamente.")
