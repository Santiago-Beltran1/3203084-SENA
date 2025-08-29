import datetime

# Obtener fecha y hora actuales
ahora = datetime.datetime.now()
print(f"Fecha y hora actuales: {ahora}")

# Crear una fecha específica
fecha_especifica = datetime.datetime(2023, 12, 31, 23, 59, 59)
print(f"Año nuevo: {fecha_especifica}")

# Calcular diferencia entre fechas
diferencia = fecha_especifica - ahora
print(f"Faltan {diferencia.days} días para año nuevo")

# Formatear fecha
formato_personalizado = ahora.strftime("%d/%m/%Y %H:%M")
print(f"Formato personalizado: {formato_personalizado}")