# Calculadora Simple

try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    print("\nOperaciones disponibles: + (suma), - (resta), * (multiplicación), / (división)")
    operacion = input("Selecciona una operación: ")

    if operacion == "+":
        resultado = num1 + num2
    elif operacion == "-":
        resultado = num1 - num2
    elif operacion == "*":
        resultado = num1 * num2
    elif operacion == "/":
        if num2 == 0:
            raise ZeroDivisionError("No se puede dividir por cero.")
        resultado = num1 / num2
    else:
        raise ValueError("Operación no válida.")


    print(f"\nResultado: {num1} {operacion} {num2} = {resultado:.2f}")

except ValueError as ve:
    print(f"Error de valor: {ve}")
except ZeroDivisionError as zde:
    print(f"Error matemático: {zde}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
