from classDirector import Director
from classGerente import Gerente
from classJefeArea import Jefe_Area

director = Director()

director.set_nombrepersona("John")
director.set_apellidopersona("Doe")
director.set_edadpersona(45)

director.setcargo("Chief Executive Officer")
director.sethorario("Nocturno")
director.setsueldo(25000)

director.set_nombre_area("Financiera")
director.set_presupuesto(800000)
director.set_nombre_departamento("Contabilidad")
director.set_no_empleados(120)

director.setRegion("Ciudad de México")
director.setPresupuesto_asignado(750000)

jefe_area = Jefe_Area()

jefe_area.set_nombrepersona("Carlos")
jefe_area.set_apellidopersona("López")
jefe_area.set_edadpersona(38)

jefe_area.setcargo("Manager")
jefe_area.sethorario("Vespertino")
jefe_area.setsueldo(18000)

jefe_area.set_nombre_area("Operaciones")
jefe_area.set_presupuesto(300000)
jefe_area.set_nombre_departamento("Logística")
jefe_area.set_no_empleados(80)

gerente = Gerente()

gerente.set_nombrepersona("Ana")
gerente.set_apellidopersona("González")
gerente.set_edadpersona(30)

gerente.setcargo("Senior Manager")
gerente.sethorario("Matutino")
gerente.setsueldo(20000)

gerente.set_nombre_area("Financiera")
gerente.set_presupuesto(450000)
gerente.set_nombre_departamento("Contabilidad")
gerente.set_no_empleados(40)

print("Información de Empleados")
print("")
director.mostrar_informacion_empleado()
print("")
jefe_area.mostrar_informacion_empleado()
print("")
gerente.mostrar_informacion_empleado()
print("")

print("\nInformación por Áreas")
print("")
director.mostrar_informacion_area()
print("")
jefe_area.mostrar_informacion_area()
print("")
gerente.mostrar_informacion_area()
