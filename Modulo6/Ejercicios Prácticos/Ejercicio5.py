#Tabla de multiplicar
#Programa que genera una tabla de multiplicar del 1 al 10 usando bucles anidados.

print("Tabla de multiplicar del 1 al 10:")
print("-" * 40)
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print()
