#Sentencias de control de bucles: break, continue, pass.

# break → sale del bucle
for i in range(10):
    if i == 5:
        break
    print("Número:", i)

# continue → salta a la siguiente iteración
for i in range(5):
    if i == 2:
        continue
    print("Se muestra:", i)

# pass → no hace nada, sirve como marcador de posición
for i in range(3):
    if i == 1:
        pass  
    print("Iteración:", i)
