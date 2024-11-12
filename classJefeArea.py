from classArea import Area
from classEmpleado import Empleado
class Jefe_Area(Area, Empleado):
    def __init__(self):
        Area.__init__(self)
        Empleado.__init__(self)
        self.objetivo_area = ""

    def get_objetivo_area(self):
        return self.objetivo_area

    def set_objetivo_area(self, objetivo_area):
        self.objetivo_area = objetivo_area

    def asignar_supervisor(self):
        print("Asignando nuevo supervisor")

    def convocar_reunion(self):
        print("Convocando a reunión")
