# Conversor de Temperatura

print("Conversor de Temperatura")
print("Escalas disponibles: Celsius (C), Fahrenheit (F), Kelvin (K)")

origen = input("Ingresa la escala de origen (C/F/K): ").upper()
destino = input("Ingresa la escala de destino (C/F/K): ").upper()
temp = float(input("Ingresa la temperatura a convertir: "))

resultado = None 

if origen == "C" and destino == "F":
    resultado = temp * 9/5 + 32
elif origen == "C" and destino == "K":
    resultado = temp + 273.15
elif origen == "F" and destino == "C":
    resultado = (temp - 32) * 5/9
elif origen == "F" and destino == "K":
    resultado = (temp - 32) * 5/9 + 273.15
elif origen == "K" and destino == "C":
    resultado = temp - 273.15
elif origen == "K" and destino == "F":
    resultado = (temp - 273.15) * 9/5 + 32
elif origen == destino:
    resultado = temp
else:
    print("Conversión no válida. Revisa las escalas ingresadas.")

if resultado is not None:
    print(f"\n{temp}°{origen} equivale a {resultado:.2f}°{destino}")