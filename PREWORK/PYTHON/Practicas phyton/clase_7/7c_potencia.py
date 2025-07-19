"""POTENCIA Implementa una función recursiva llamada potencia que calcule el resultado de elevar 
un número a una potencia dada. Puedes asumir que tanto el número como la potencia son enteros no 
negativos."""

def potencia(base, exponente):
    #funcion q nos calcula la potencia dado dos numeros, el numero y la potecnia de dicho numero
    if exponente==0:
     print("caso base alcanzado")
     return 1
    else:
       resultado=base*potencia(base, exponente-1)
       print(f"{base}^{exponente} = {resultado}")
       return resultado
    
numero=int(input("Introduce el numero: "))
pot=int(input("Introduce la potencia: "))

print(f"\nResultado final: {potencia(numero, pot)}")

"""En la recursión, empieza por el exponente que le das, y va restando 1 en cada llamada hasta 
llegar a 0, que es el caso base.

Por ejemplo, si haces potencia(3, 4), la función sigue este orden:

1. potencia(3, 4) llama a  
2. potencia(3, 3) llama a  
3. potencia(3, 2) llama a  
4. potencia(3, 1) llama a  
5. potencia(3, 0) → aquí se devuelve 1  
Luego la recursión se va resolviendo hacia arriba:

- 3 * 1 = 3
- 3 * 3 = 9
- 3 * 9 = 27
- 3 * 27 = 81

Así que el resultado es 3^4 = 81.

Resumen: no empieza en 0, empieza en el valor que tú le pases (por ejemplo 4), pero al ser 
recursivo, va bajando hasta llegar a 0."""