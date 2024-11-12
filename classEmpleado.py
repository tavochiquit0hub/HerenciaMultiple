from classPersona import Persona

class Empleado(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.__cargo = ""
        self.__horario = ""
        self.__sueldo = 0

    def getcargo(self):
        return self.__cargo

    def setcargo(self, cargo):
        self.__cargo = cargo

    def gethorario(self):
        return self.__horario

    def sethorario(self, horario):
        self.__horario = horario

    def getsueldo(self):
        return self.__sueldo

    def setsueldo(self, sueldo):
        self.__sueldo = sueldo

    def cambiar_salario(self):
        print("Solicitando aprobación para ajuste salarial")

    def solicitar_permiso(self):
        print("Solicitando permiso para ausencia o vacaciones")

    def mostrar_informacion_empleado(self):
        print(f"Nombre: {self.get_nombrepersona()}, Apellido: {self.get_apellidopersona()}\n"
              f"Edad: {self.get_edadpersona()}, Puesto: {self.getcargo()}\n"
              f"Horario: {self.gethorario()}, Sueldo: {self.getsueldo()}")
