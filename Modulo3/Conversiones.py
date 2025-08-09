# Datos iniciales
datos_iniciales = [1, 2, 2, 3, 4, 4, 5]
print(f"Datos iniciales (lista): {datos_iniciales}")

# Convertir lista a tupla
tupla = tuple(datos_iniciales)
print(f"Como tupla: {tupla}")
# Resultado: (1, 2, 2, 3, 4, 4, 5)

# Convertir lista a conjunto (elimina duplicados)
conjunto = set(datos_iniciales)
print(f"Como conjunto: {conjunto}")
# Resultado: {1, 2, 3, 4, 5}

# Convertir lista a diccionario (necesita pares clave-valor)
# Usamos enumerate para crear pares (índice, valor)
diccionario = dict(enumerate(datos_iniciales))
print(f"Como diccionario: {diccionario}")
# Resultado: {0: 1, 1: 2, 2: 2, 3: 3, 4: 4, 5: 4, 6: 5}

# Convertir conjunto a lista (útil después de eliminar duplicados)
lista_sin_duplicados = list(conjunto)
print(f"Conjunto convertido a lista: {lista_sin_duplicados}")
# Resultado: [1, 2, 3, 4, 5]

# Convertir diccionario a lista de claves, valores o items
claves = list(diccionario.keys())
valores = list(diccionario.values())
items = list(diccionario.items())
print(f"Claves del diccionario: {claves}")
print(f"Valores del diccionario: {valores}")
print(f"Items del diccionario: {items}")