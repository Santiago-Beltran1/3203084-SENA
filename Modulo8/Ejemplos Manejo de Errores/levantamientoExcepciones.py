#Levantamiento de Excepciones - Se hace uso de raise para generar la excepción personalizada.

def verificar_edad(edad):
    if edad < 0:
        # Se levanta una excepción de tipo ValueError con un mensaje personalizado
        raise ValueError("La edad no puede ser un número negativo.")
    elif edad > 140:
        raise ValueError("La edad es absurdamente alta para un ser humano.")
    else:
        print(f"La edad de {edad} años es válida.")

try:
    # Llamada a la función con un valor que causa una excepción
    verificar_edad(-5)
    
except ValueError as error_msg:
    # Capturar y mostrar el mensaje de la excepción
    print(f"Se ha producido un error: {error_msg}")