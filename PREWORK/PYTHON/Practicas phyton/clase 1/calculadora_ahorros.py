"""tus ahorros anuales. El programa deberá calcular cuánto puede ahorrar una persona dado
sus ingresos por hora, sus horas trabajadas y su gasto de vida semanal."""

# 1. Primero haremos que el programa nos pida nuestro nombre y después imprima un saludo por
# pantalla de tipo: ‘Hola <Nombre>

print("Bienvenido a la calculadora de ahorros")
nombre = input("¿Cuál es tu nombre? ")
print("Hola " + nombre, ", bienvenido a la calculadora de ahorros")

# 2.Guarda el dinero ganado por hora y las horas trabajadas en la semana en dos variables diferentes

dinero_ganado_hora = float(input("¿Cuánto dinero ganas por hora? "))
horas_trabajadas = float(input("¿Cuántas horas trabajas a la semana? "))

# 3.-Multiplica ambas variables para obtener el salario semanal

salario_semanal = dinero_ganado_hora * horas_trabajadas

# 4. Ahora calcula las ganancias anuales. Guarda el valor en una variable.

ganancias_anuales = salario_semanal * 52

# 5.-Ahora imprime por pantalla un mensaje del tipo: ‘<Nombre> tiene unas ganancias anuales
# de: <cantidad> euros’

print(nombre, "tienes unas ganancias anuales de: ", ganancias_anuales, "euros")

# 6. Pide los gastos semanales por pantalla y guárdalos en una variable.

gastos_semanales = float(input("¿Cuánto gastas a la semana? "))

# 7. Calcula los gastos anuales y guárdalos en una variable.

gastos_anuales = gastos_semanales * 52

# 8. Los ahorros anuales serán la resta entre lo ganado durante el año menos los gastos anuales.

ahorros_anuales = ganancias_anuales - gastos_anuales

print("Tus ahorros anuales son: ", ahorros_anuales, "euros")

# 9.¿Si el usuario decidiese trabajar a tiempo parcial (25 horas semanales) y
# decidiese reducir sus gastos a 3/4 de lo que gastaba antes, tendría su cliente dinero para
# sus gastos?

horas_trabajadas = 25

salario_semanal = dinero_ganado_hora * horas_trabajadas
ganancias_anuales = salario_semanal * 52

gastos_semanales = gastos_semanales * 3 / 4
gastos_anuales = gastos_semanales * 52

ahorros_anuales = ganancias_anuales - gastos_anuales

print(
    "Tus ahorros anuales son con la jornada reducida (25 horas) \
y reduciendo tus gastos 3/4 partes de:",
    ahorros_anuales,
    "euros",
)
