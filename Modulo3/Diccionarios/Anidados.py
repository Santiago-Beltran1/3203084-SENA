# Estructura de datos compleja con diccionarios anidados
inventario = {
    "electronica": {
        "smartphones": {
            "iPhone": {"stock": 15, "precio": 999.99},
            "Samsung": {"stock": 20, "precio": 899.99},
            "Xiaomi": {"stock": 30, "precio": 499.99},
        },
        "laptops": {
            "Dell": {"stock": 10, "precio": 1299.99},
            "HP": {"stock": 8, "precio": 1099.99}
        }
    },
    "hogar": {
        "muebles": {
            "sillas": {"stock": 50, "precio": 79.99},
            "mesas": {"stock": 25, "precio": 199.99}
        }
    }
}

# Acceso a datos anidados
precio_iphone = inventario["electronica"]["smartphones"]["iPhone"]["precio"]
print(f"Precio del iPhone: ${precio_iphone}")
# Resultado: Precio del iPhone: $999.99

# Modificación de datos anidados
inventario["electronica"]["laptops"]["Dell"]["stock"] -= 1
print(f"Stock actualizado de Dell: {inventario['electronica']['laptops']['Dell']['stock']}")
# Resultado: Stock actualizado de Dell: 9