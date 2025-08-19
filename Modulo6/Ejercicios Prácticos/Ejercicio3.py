#Invertir Cadena
#Programa que invierte una cadena de texto sin usar la función reversed o slicing.

texto = "Python es divertido"
invertido = ""

for caracter in texto:
    invertido = caracter + invertido

print(invertido)
