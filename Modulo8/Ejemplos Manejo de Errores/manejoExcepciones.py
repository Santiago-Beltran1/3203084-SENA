#Manejo de Excepciones

#Uso de try
try:
    # Código que podría causar un error
    numero = int(input("Introduce un número entero: "))
    resultado = 10 / numero
    print(f"El resultado es {resultado}")


#Uso de except
except ValueError:
    # Este bloque se ejecuta si ocurre un ValueError (por ejemplo, si el usuario no introduce un número)
    print("Error: Debes introducir un número entero válido.")
except ZeroDivisionError:
    # Este bloque se ejecuta si ocurre un ZeroDivisionError (por ejemplo, si el usuario introduce 0)
    print("Error: No se puede dividir por cero.")