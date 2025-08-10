# Sistema de recomendación
historial = ["ropa", "zapatos", "camiseta"]

preferencia = input("¿Qué tipo de producto te interesa? ").lower()

if preferencia in historial:
    print(f"Te recomendamos más productos de {preferencia}.")
elif preferencia == "tecnología":
    print("Recomendación: laptops, smartphones, tablets.")
elif preferencia == "hogar":
    print("Recomendación: muebles, decoración, electrodomésticos.")
else:
    print("No tenemos recomendaciones para esa categoría.")
