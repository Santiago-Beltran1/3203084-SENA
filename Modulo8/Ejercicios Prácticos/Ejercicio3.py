#Acceso a un diccionario

diccionario = {"manzana": 1, "pera": 2, "uva": 3}

try:
    # Pedir al usuario la clave a buscar
    clave_buscada = input("Introduce una fruta para obtener su valor: ")
    
    # Intentar acceder al valor de la clave
    valor = diccionario[clave_buscada]
    
    print(f"El valor para '{clave_buscada}' es {valor}.")
    
except KeyError:
    # Este bloque se ejecuta si la clave no se encuentra en el diccionario
    print(f"Error: La fruta '{clave_buscada}' no se encuentra en el diccionario.")
except Exception as e:
    # Capturar cualquier otro error
    print(f"Ocurrió un error: {e}")