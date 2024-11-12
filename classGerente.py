from classEmpleado import Empleado
from classArea import Area
class Gerente(Area, Empleado):
    def __init__(self):
        Area.__init__(self)
        Empleado.__init__(self)
        self.cargo = ""
        self.objetivo_estrategico = ""

    def get_cargo(self):
        return self.cargo

    def get_objetivo_estrategico(self):
        return self.objetivo_estrategico

    def set_cargo(self, cargo):
        self.cargo = cargo

    def set_objetivo_estrategico(self, objetivo_estrategico):
        self.objetivo_estrategico = objetivo_estrategico

    def evaluar_empleados(self):
        print("Evaluando el desempeño de los empleados")

    def dar_feedback(self):
        print("Dando retroalimentación positiva")
