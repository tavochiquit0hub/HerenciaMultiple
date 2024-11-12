from classArea import Area
from classEmpleado import Empleado
class Director(Area, Empleado):
    def __init__(self):
        Area.__init__(self)
        Empleado.__init__(self)
        self.__region = ""
        self.__empleados = 0
        self.__presupuesto_asignado = 0

    def setEmpleados(self, empleados):
        self.__empleados = empleados

    def setPresupuesto_asignado(self, presupuesto_asignado):
        self.__presupuesto_asignado = presupuesto_asignado

    def getEmpleados(self):
        return self.__empleados

    def getPresupuesto_asignado(self):
        return self.__presupuesto_asignado

    def setRegion(self, region):
        self.__region = region

    def getRegion(self):
        return self.__region

    def tomar_decision(self):
        print("Tomando decisiones estratégicas")

    def convocar_asamblea(self):
        print("Convocando a asamblea general")

    def informacion_director(self):
        print(f"Nombre: {self.get_nombrepersona()} {self.get_apellidopersona()}")
