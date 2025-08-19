#Funciones anónimas (lambda) - Sintaxis.

# Función lambda
doble = lambda x: x * 2
print(doble(5))

# Uso de lambda con map
numeros = [1, 2, 3, 4]
numeros_doblados = list(map(lambda x: x * 2, numeros))
print(numeros_doblados)
