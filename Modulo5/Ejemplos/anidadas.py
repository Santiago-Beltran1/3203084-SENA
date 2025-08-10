#Ejemplo de if dentro de if - condiciones anidadas
usuario = input("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese su contraseña: ")

if usuario == "admin":
    if contraseña == "1234":
        print("Acceso concedido.")
    else:
        print("Contraseña incorrecta.")
else:
    print("Usuario no válido.")
