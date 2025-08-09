# Obtener el numero de elementos
mi_lista = ['Primer elemento nuevo', 2, 3, True, 5.5, 100]
cantidad_elementos = len(mi_lista)
print(f"La lista ahora tiene {cantidad_elementos} elementos.")
# Resultado:
# La lista ahora tiene 6 elementos.


# Cambiar el valor de un elemento existente
mi_lista = [1, 2, 3, True, 5.5, 100]
mi_lista[0] = "Primer elemento nuevo"
print(f"Lista después de modificar: {mi_lista}")
# Resultado:
# Lista después de modificar: ['Primer elemento nuevo', 2, 3, True, 5.5, 100]


# Elimina un elemento por su índice y lo devuelve
tareas = ["Estudiar", "Comprar", "Cocinar", "Limpiar"]
tarea_urgente = tareas.pop(1)  # Elimina "Comprar"
print(f"Tarea eliminada: {tarea_urgente}")
print(f"Lista después: {tareas}")
# Resultado:
# Tarea eliminada: Comprar
# Lista después: ['Estudiar', 'Cocinar', 'Limpiar']


# Sin argumentos, elimina el último elemento
ultima_tarea = tareas.pop()  # Elimina "Limpiar"
print(f"Última tarea: {ultima_tarea}")
print(f"Lista final: {tareas}")
# Resultado:
# Última tarea: Limpiar
# Lista final: ['Estudiar', 'Cocinar']


# Inserta un elemento en una posición específica
numeros = [1, 2, 4, 5]
numeros.insert(2, 3)  # Inserta 3 en índice 2
print(f"Después de insert(2, 3): {numeros}")
# Resultado:
# Después de insert(2, 3): [1, 2, 3, 4, 5]


# Insertar al principio
numeros.insert(0, 0)  # Inserta 0 al inicio
print(f"Después de insert(0, 0): {numeros}")
# Resultado:
# Después de insert(0, 0): [0, 1, 2, 3, 4, 5]


# Ordena los elementos de la lista en su lugar de menor a mayor
numeros_desordenados = [5, 2, 8, 1, 9]
numeros_desordenados.sort()
print(f"Después de sort() (ascendente): {numeros_desordenados}")
# Resultado: Después de sort() (ascendente): [1, 2, 5, 8, 9]


# Ordena los elementos en orden inverso (descendente)
nombres = ["Carlos", "Ana", "David", "Beatriz"]
nombres.sort(reverse=True)
print(f"Orden descendente: {nombres}")
# Resultado: Orden descendente: ['David', 'Carlos', 'Beatriz', 'Ana']


# Simplemente invierte el orden actual de la lista (no ordena)
secuencia = [1, 2, 3, 4, 5]
secuencia.reverse()
print(f"Después de reverse(): {secuencia}")
# Resultado: Después de reverse(): [5, 4, 3, 2, 1]


# Añade todos los elementos de otro iterable
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)
print(f"Después de extend: {lista1}")
# Resultado: Después de extend: [1, 2, 3, 4, 5, 6]
