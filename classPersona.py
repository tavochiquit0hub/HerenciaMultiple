class Persona:
    def __init__(self):
        self.__nombrepersona = ""
        self.__apellidopersona = ""
        self.__edadpersona = 0

    def get_nombrepersona(self):
        return self.__nombrepersona

    def set_nombrepersona(self, nombrepersona):
        self.__nombrepersona = nombrepersona

    def get_apellidopersona(self):
        return self.__apellidopersona

    def set_apellidopersona(self, apellidopersona):
        self.__apellidopersona = apellidopersona

    def get_edadpersona(self):
        return self.__edadpersona

    def set_edadpersona(self, edadpersona):
        self.__edadpersona = edadpersona
