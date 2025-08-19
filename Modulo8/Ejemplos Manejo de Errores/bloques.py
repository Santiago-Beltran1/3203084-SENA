#Bloques else y finally

#El bloque else se ejecuta si no ocurre ninguna excepción en el bloque try. 

#El bloque finally siempre se ejecuta, sin importar si hubo una excepción o no.

try:
    # Pedir al usuario que ingrese un número
    num_str = input("Introduce un número: ")
    num = int(num_str)
    
except ValueError:
    # Manejar el error si la entrada no es un número válido
    print("Eso no es un número. Intenta de nuevo.")
    
else:
    # Este bloque se ejecuta solo si no hay errores en el 'try'
    print(f"¡Éxito! El número ingresado fue {num}.")
    
finally:
    # Este bloque se ejecuta siempre, haya o no una excepción
    print("El manejo de la excepción ha terminado.")