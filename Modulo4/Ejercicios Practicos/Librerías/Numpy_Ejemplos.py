import numpy as np

# Crear un arreglo
arr = np.array([1, 2, 3, 4, 5])
print("Arreglo:", arr)

# Suma de todos los elementos
print("Suma:", np.sum(arr))

# Promedio
print("Promedio:", np.mean(arr))

# Raíz cuadrada de cada elemento
print("Raíz cuadrada:", np.sqrt(arr))

# Matriz 2x2
matriz = np.array([[1, 2], [3, 4]])
print("Matriz:")
print(matriz)

# Multiplicación de matrices
matriz2 = np.array([[5, 6], [7, 8]])
print("Multiplicación de matrices:")
print(np.dot(matriz, matriz2))
