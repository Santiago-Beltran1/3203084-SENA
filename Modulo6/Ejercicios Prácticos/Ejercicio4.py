#Números primos
#Función que determine si un número es primo usando bucle for y la sentencia break cuando es apropiado.

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Probamos con algunos números
for n in [2, 3, 4, 5, 6, 7, 11, 13, 15, 17]:
    print(f"{n} es primo: {es_primo(n)}")
