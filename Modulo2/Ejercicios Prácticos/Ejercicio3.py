# Manipulación de Cadenas

frase = input("Ingresa una frase: ")

num_caracteres = len(frase)

palabras = frase.split()
num_palabras = len(palabras)

mayusculas = frase.upper()
minusculas = frase.lower()

inversa = frase[::-1]

palabra_buscar = input("Ingresa la palabra que deseas buscar: ")
conteo_palabra = frase.lower().count(palabra_buscar.lower())

palabra_antigua = input("Palabra que deseas reemplazar: ")
palabra_nueva = input("Palabra nueva: ")
frase_reemplazada = frase.replace(palabra_antigua, palabra_nueva)

print("\n--- Resultados ---")
print(f"Número de caracteres: {num_caracteres}")
print(f"Número de palabras: {num_palabras}")
print(f"Frase en mayúsculas: {mayusculas}")
print(f"Frase en minúsculas: {minusculas}")
print(f"Frase en orden inverso: {inversa}")
print(f"La palabra '{palabra_buscar}' aparece {conteo_palabra} vez/veces")
print(f"Frase con reemplazo: {frase_reemplazada}")
