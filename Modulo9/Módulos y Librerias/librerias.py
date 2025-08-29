# Pregunta: ¿Cómo instalar y usar librerías de terceros?
# Respuesta: Se instalan con "pip install <nombre>" desde la consola.
# Ejemplo: pip install numpy pandas

import numpy as np
import pandas as pd

print("\nEjemplo usando librerías de terceros (NumPy y Pandas):")

# Con NumPy
array = np.array([1, 2, 3, 4, 5])
print("Array creado con NumPy:", array)

# Con Pandas
datos = {"Nombre": ["Ana", "Luis", "Juan"], "Edad": [23, 30, 18]}
df = pd.DataFrame(datos)
print("\nDataFrame creado con Pandas:")
print(df)
