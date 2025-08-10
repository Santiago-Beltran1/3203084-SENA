# Analizador de datos 
datos = [10, 20, 15, 30, 25]

promedio = sum(datos) / len(datos)

print(f"Datos: {datos}")
print(f"Promedio: {promedio}")

if promedio < 15:
    print("Datos bajos, sugerencia: generar gráfico de barras.")
elif promedio <= 25:
    print("Datos moderados, sugerencia: generar gráfico de líneas.")
else:
    print("Datos altos, sugerencia: generar gráfico circular.")
