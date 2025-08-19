#Errores Comunes

# Error de sintaxis (SyntaxError): Falta un paréntesis
# print("Hola mundo" 

# Error de tipo (TypeError): Intentar sumar un entero con un string
# print(5 + "hola")

# Error de nombre (NameError): Usar una variable no definida
# print(mi_variable)

# Para ejecutar, descomente cada línea de error individualmente.

# El código a continuación no tiene errores y se ejecutará correctamente.
print("El siguiente código muestra cómo evitar errores comunes.")
x = 5
y = "10"

# Convertimos el string a entero antes de sumar
z = x + int(y)
print(f"La suma de {x} y {y} es {z}")