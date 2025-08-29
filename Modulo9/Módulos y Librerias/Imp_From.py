#¿Cómo importar funciones específicas de un módulo?
# Usando "from <módulo> import <función>"

import math
from math import factorial
import random as rnd   

print("\nEjemplo de importaciones:")
print("Usando 'import': raíz cuadrada de 36 =", math.sqrt(36))
print("Usando 'from': factorial de 5 =", factorial(5))
print("Usando alias: número aleatorio entre 1 y 10 =", rnd.randint(1, 10))
