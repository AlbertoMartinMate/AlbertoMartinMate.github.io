

""" Crea un programa en el que se pregunte al usuario por una frase y una letra, y muestre por
pantalla el número de veces que aparece la letra en la frase. """

frase= input("Introduce una frase: ")
caracter= input("Introduce la letra que quieres que cuente en dicha frase: ")
num_letra = 0


for letra in frase:
     if letra==caracter:
        num_letra = num_letra +1 #num_letra +=1


print ("La letra", caracter.upper(), "aparece", num_letra, "veces" )