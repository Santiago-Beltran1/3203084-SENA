#Argumentos y parámetros - Posicionales, por palabra clave y con valor predeterminado.

def estudiante(nombre, edad, carrera="Ingeniería"):
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Carrera:", carrera)

# Argumentos posicionales
estudiante("Lucía", 20)

# Argumentos por palabra clave
estudiante(nombre="Pedro", edad=22, carrera="Derecho")

# Argumentos con valor predeterminado
estudiante("Ana", 21)
