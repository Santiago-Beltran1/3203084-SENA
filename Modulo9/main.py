import operaciones
import numpy as np

print("\nEjemplo práctico combinando módulos propios y librerías externas:")

# Usando nuestro módulo
print("Multiplicación 6 * 7 =", operaciones.multiplicar(6, 7))
print("División 10 / 2 =", operaciones.dividir(10, 2))

# Usando NumPy
numeros = [4, 8, 15, 16, 23, 42]
print("La media de la lista con NumPy es:", np.mean(numeros))
