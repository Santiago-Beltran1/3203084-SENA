# Funciones que convierten temperaturas y devuelven el resultado

def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

def celsius_a_kelvin(c):
    return c + 273.15

def kelvin_a_celsius(k):
    return k - 273.15

# Función sin retorno que imprime un menú
def mostrar_menu():
    print("Conversor de Temperaturas")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Celsius a Kelvin")
    print("4. Kelvin a Celsius")
    print("5. Salir")

def conversor():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ")

        if opcion == '5':
            print("Saliendo del conversor...")
            break
        
        if opcion in ('1', '2', '3', '4'):
            try:
                temp = float(input("Ingresa la temperatura a convertir: "))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue
            
            if opcion == '1':
                resultado = celsius_a_fahrenheit(temp)
                print(f"{temp} °C = {resultado:.2f} °F")
            elif opcion == '2':
                resultado = fahrenheit_a_celsius(temp)
                print(f"{temp} °F = {resultado:.2f} °C")
            elif opcion == '3':
                resultado = celsius_a_kelvin(temp)
                print(f"{temp} °C = {resultado:.2f} K")
            elif opcion == '4':
                resultado = kelvin_a_celsius(temp)
                print(f"{temp} K = {resultado:.2f} °C")
        else:
            print("Opción inválida, intenta de nuevo.")

# Ejecutar el conversor
conversor()
