#Variables Y Tipos De Datos

#4. Conversión de Tipos

#int() convierte a entero:
numero = int("10")
print(numero, type(numero))  

#float() convierte a flotante:
decimal = float("3.14")
print(decimal, type(decimal)) 

#str() – convierte a cadena de texto:
texto = str(100)
print(texto, type(texto)) 

#bool(): Convierte a booleano cualquier valor a True o False según si está "vacío" o no.
print(bool(0))         # False
print(bool(5))         # True
print(bool(""))        # False
print(bool("Hola"))    # True

#list(): Convierte cualquier iterable (como una cadena o una tupla) en una lista.
texto = "hola"
print(list(texto))   

#tuple(): Convierte a tupla.
lista = [1, 2, 3]
print(tuple(lista)) 

#set(): Convierte a conjunto pero sin elementos repetidos.
repetidos = [1, 2, 2, 3, 3, 3]
print(set(repetidos))  




