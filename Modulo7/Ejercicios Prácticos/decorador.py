#Decorador para medir el tiempo
import time

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()  # Tiempo antes de ejecutar la función
        resultado = func(*args, **kwargs)  # Ejecuta la función original
        fin = time.time()  # Tiempo después de ejecutarla
        print(f"La función '{func.__name__}' se ejecutó en {fin - inicio:.6f} segundos.")
        return resultado
    return wrapper

# Ejemplo de uso del decorador
@medir_tiempo
def suma_larga(lista):
    return sum(lista)

# Llamada a la función decorada
resultado = suma_larga(range(1_000_000))
print("Resultado:", resultado)
