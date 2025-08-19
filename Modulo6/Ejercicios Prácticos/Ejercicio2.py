#Factorial
#Función que calcula el factorial de un número usando un bucle while.

def factorial(n):
    resultado = 1
    while n > 0:
        resultado *= n
        n -= 1
    return resultado

print(factorial(5))
