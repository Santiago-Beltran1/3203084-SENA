# Crear un conjunto
frutas = {"manzana", "banana", "cereza"}

# Agregar un elemento
frutas.add("naranja")

# Intentar agregar un duplicado (no se agrega)
frutas.add("manzana")

# Eliminar un elemento
frutas.remove("banana")

# Recorrer el conjunto
for fruta in frutas:
    print(fruta)

# Comprobar si un elemento está en el conjunto
print("cereza" in frutas) 

print(frutas)