# Creación estándar con paréntesis
colores = ("rojo", "verde", "azul")
print(colores)
# Resultado: ('rojo', 'verde', 'azul')


# Tupla con un solo elemento (¡necesita la coma!)
singleton = (42,)
print(singleton)        # Resultado: (42,)
print(type(singleton))  # Resultado: <class 'tuple'>
# Sin la coma sería un entero, no una tupla


# Python permite omitir los paréntesis
dias = "lunes", "martes", "miércoles"
print(dias)       # Resultado: ('lunes', 'martes', 'miércoles')
print(type(dias)) # Resultado: <class 'tuple'>


# Desempaquetado directo
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")  # Resultado: x=1, y=2, z=3


# Convertir otros iterables en tuplas
lista = [1, 2, 3]
tupla_desde_lista = tuple(lista)
print(tupla_desde_lista)  # Resultado: (1, 2, 3)


# Tupla vacía
tupla_vacia = tuple()
print(tupla_vacia)   # Resultado: ()