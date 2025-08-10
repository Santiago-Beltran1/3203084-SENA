#And, or, not
edad = int(input("Ingrese su edad: "))
tiene_licencia = input("¿Tiene licencia de conducir? (sí/no): ").lower()

if edad >= 18 and tiene_licencia == "sí":
    print("Puedes conducir un vehículo.")
elif edad >= 18 and tiene_licencia == "no":
    print("Eres mayor de edad, pero necesitas licencia.")
elif edad < 18 or not (tiene_licencia == "sí"):
    print("No puedes conducir.")
