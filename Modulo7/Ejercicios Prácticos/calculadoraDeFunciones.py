# Definición de funciones con parámetros y retorno
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    else:
        return a / b

# Función sin retorno que solo imprime
def mostrar_resultado(resultado):
    print("Resultado:", resultado)

# Operación con lambda como ejemplo de función anónima
potencia = lambda base, exp: base ** exp

def calculadora():
    print("Calculadora de funciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia (con lambda)")
    
    while True:
        opcion = input("Elige una opción (1-5) o 'salir' para terminar: ")
        
        if opcion == 'salir':
            print("Saliendo de la calculadora...")
            break
        
        if opcion in ('1', '2', '3', '4', '5'):
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
            except ValueError:
                print("Por favor, ingresa números válidos.")
                continue
            
            if opcion == '1':
                res = suma(num1, num2)
            elif opcion == '2':
                res = resta(num1, num2)
            elif opcion == '3':
                res = multiplicacion(num1, num2)
            elif opcion == '4':
                res = division(num1, num2)
            elif opcion == '5':
                res = potencia(num1, num2)
            
            mostrar_resultado(res)
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar la calculadora
calculadora()
