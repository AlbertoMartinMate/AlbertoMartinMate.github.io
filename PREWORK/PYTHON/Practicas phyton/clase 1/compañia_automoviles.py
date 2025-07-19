# Crea un programa donde el usuario introduzca el numero de coches vendidos de cada tipo ese
# mes  y que le devuelva la cantidad en euros a comisionar ese mes

# precio coches

serie1 = float(20000)
seriePlus = float(35000)
todoterreno = float(60000)

# pedimos el número de coches vendidos de cada tipo

vendidos_serie1 = float((input)("¿Cuantos serie1 se han vendido este mes?"))

vendidos_seriePlus = float((input)("¿Cuantos serie Plus se han vendido este mes?"))

vendidos_todoterreno = float((input)("¿Cuantos todoterreno se han vendido este mes?"))

# calculamos la comision recibida por cada tipo de coche

comision_serie1 = (serie1 * vendidos_serie1) * 0.03
comision_seriePlus = (seriePlus * vendidos_seriePlus) * 0.05
comision_todoterreno = (todoterreno * vendidos_todoterreno) * 0.07

print((comision_serie1), "euros")
print((comision_seriePlus), "euros")
print((comision_todoterreno), "euros")

total = comision_todoterreno + comision_serie1 + comision_seriePlus

print((total), "euros, el total ganado este mes")
