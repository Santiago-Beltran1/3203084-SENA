#Conversor de edad

import datetime

try:
    # Pedir al usuario su año de nacimiento
    anio_nacimiento = int(input("Introduce tu año de nacimiento: "))
    
    # Obtener el año actual
    anio_actual = datetime.date.today().year
    
    # Calcular la edad
    edad = anio_actual - anio_nacimiento
    
    print(f"Tu edad es de {edad} años.")
    
except ValueError:
    # Este bloque se ejecuta si el usuario introduce un texto en lugar de un número
    print("Error: Por favor, introduce un año válido como un número entero.")
except Exception as e:
    # Capturar cualquier otro error inesperado
    print(f"Ocurrió un error inesperado: {e}")