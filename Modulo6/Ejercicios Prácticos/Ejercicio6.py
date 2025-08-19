#Secuencia de Fibonacci
#Función que genera los primeros números de la secuencia de Fibonacci usando un bucle while.

def fibonacci(n):
    secuencia = []
    a, b = 0, 1
    contador = 0
    while contador < n:
        secuencia.append(a)
        a, b = b, a + b
        contador += 1
    return secuencia

print(fibonacci(10))
