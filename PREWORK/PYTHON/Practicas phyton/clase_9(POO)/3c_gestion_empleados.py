"""Supongamos que estás construyendo un sistema de gestión de empleados
para una empresa. Crea un sistema de clases que maneje la información de
los empleados, incluyendo empleados a tiempo completo y empleados a
tiempo parcial.
- Clase base: `Empleado`
 - Atributos: nombre, apellido, salario base
- Clase derivada: `EmpleadoTiempoCompleto` (hereda de `Empleado`)
 - Atributo adicional: bono anual
- Clase derivada: `EmpleadoTiempoParcial` (hereda de `Empleado`)
 - Atributo adicional: horas trabajadas por semana
Resuelve el problema creando instancias de estas clases y calculando los
salarios totales para diferentes tipos de empleados."""

class Empleado:
    """Creamos las caracteristicas básicas de empleado"""
    def __init__(self, nombre, apellido, salario=1000):
        self.nombre=nombre
        self.apellido=apellido
        self.salario=salario
    
    def sueldo_anual(self):
        return self.salario * 12 
    
    def mostramos_info(self):
        print(f"El empleado {self.nombre} {self.apellido} va a tener unas ganancias anuales de {self.sueldo_anual()} Euros")


class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, apellido, bonus, salario=1000):
        super().__init__(nombre, apellido, salario)
        self.bonus=bonus
    
    def sueldo_anual(self):
        return super().sueldo_anual() + self.bonus
    

class EmpleadoTiempoParcial(Empleado):
    def __init__(self, nombre, apellido, horas_semana, salario=1000):
        super().__init__(nombre, apellido, salario)
        self.horas_semana=horas_semana
    
    def sueldo_anual(self):
        return (super().sueldo_anual() * self.horas_semana)/40


#Ejemplo de uso
nombre1=input("Por favor introduce tu nombre: ")
empleado1=EmpleadoTiempoCompleto(nombre1, "Martinez", 2100)
empleado1.mostramos_info()
empleado2=EmpleadoTiempoParcial("Juanito", "Martinez", 24, 1200)
empleado2.mostramos_info()