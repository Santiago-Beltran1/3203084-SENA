operadores = {
    "suma": "+",
    "resta": "-",
    "multiplicacion": "*",
    "division": "/"
}

print("=== CALCULADORA ===")

opcion = input("Elige la operación (suma, resta, multiplicacion, division): ").lower()
n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))

if opcion == "suma":
    resultado = n1 + n2
elif opcion == "resta":
    resultado = n1 - n2
elif opcion == "multiplicacion":
    resultado = n1 * n2
elif opcion == "division":
    if n2 != 0:
        resultado = n1 / n2
    else:
        resultado = "No se puede dividir entre cero"
else:
    resultado = "Operación no válida"

print(f"Resultado: {resultado}")
