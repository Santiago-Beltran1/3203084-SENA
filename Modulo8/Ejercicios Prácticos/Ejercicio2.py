#Suma de dos números

try:
    # Pedir al usuario dos números
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    
    # Calcular la suma
    suma = num1 + num2
    
    print(f"La suma de {num1} y {num2} es {suma}.")
    
except ValueError:
    # Este bloque se ejecuta si la entrada no puede convertirse a un número (int o float)
    print("Error: Por favor, introduce solo números.")
except Exception as e:
    # Capturar cualquier otro tipo de error
    print(f"Ocurrió un error: {e}")