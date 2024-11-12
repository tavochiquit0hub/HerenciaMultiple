from classDepartamento import Departamento
class Area(Departamento):
    def __init__(self):
        Departamento.__init__(self)
        self.__nombre_area = ""
        self.__presupuesto = 0

    def get_nombre_area(self):
        return self.__nombre_area

    def set_nombre_area(self, nombre_area):
        self.__nombre_area = nombre_area

    def get_presupuesto(self):
        return self.__presupuesto

    def set_presupuesto(self, presupuesto):
        self.__presupuesto = presupuesto

    def generar_reporte(self):
        print(f"{self.__nombre_area} ha generado un reporte")

    def asignar_presupuesto(self):
        print(f"Se asignó un presupuesto de {self.__presupuesto} a esta área")

    def mostrar_informacion_area(self):
        print(f"Nombre del Área: {self.__nombre_area}, Presupuesto: {self.__presupuesto}\n"
              f"Departamento: {self.get_nombre_departamento()}, Empleados: {self.get_no_empleados()}")
