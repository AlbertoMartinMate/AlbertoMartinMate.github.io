"""Para tributar en un determinado país es necesario ser mayor de edad y cobrar más de 1000 euros
al mes. Además los tramos impositivos de la renta anual son los siguientes:
 RENTA
 Menos de 15.000 eu
 Entre 15.000 y 25.000 eu
 Entre 25.000 y 35.000 eu
 Entre 35.000 y 60.000 eu
 Más de 60.000 eu
 TIPO IMPOSITIVO
 5%
 15%
 20%
 30%
 45%
 Escribe un script que primero compruebe si eres susceptible de que se te aplique algún tipo
impositivo y en caso afirmativo imprima por pantalla cuál te tocaría"""

# pedimos los datos al usuario. edad e ingresos
mayor_edad = input("¿Eres mayor de edad? Si/No: ")
mayor_edad = mayor_edad.lower()
sueldo = int(input("¿Cuál es tu sueldo mensual?"))

# calculamos el sueldo anual para saber si tiene q tributar y la cantidad

sueldo_anual = sueldo * 12

# hacemos un condicional para comprobar si se cumplen los dos requisitos

if (mayor_edad == "si") and (sueldo >= 1000):

    print("Tienes la obligación a tributar")

    # si tiene q tributar, calculamos la cantidad

    if sueldo_anual < 15000:
        print("Debes pagar un 5% de impuesto", sueldo_anual * 0.05, "euros")

    elif (sueldo_anual >= 15000) and (sueldo_anual < 25000):
        print("Debes pagar un 15% de impuesto", sueldo_anual * 0.15, "euros")

    elif (sueldo_anual >= 25000) and (sueldo_anual < 35000):
        print("Debes pagar un 20% de impuesto", sueldo_anual * 0.20, "euros")

    elif (sueldo_anual >= 35000) and (sueldo_anual < 60000):
        print("Debes pagar un 30% de impuesto", sueldo_anual * 0.30, "euros")

    else:
        print("Debes pagar un 45% de impuesto", sueldo_anual * 0.45, "euros")

else:
    print("No tiene la obligación de tributar")
